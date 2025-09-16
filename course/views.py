from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CourseSerializer
from django.shortcuts import get_object_or_404
from .models import Course
from tutor_management.models import Tutor
from .serializers import SubscribeSerializer
from student_management.models import Student

# Create your views here.
class CourseManagement(APIView):
    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response({"message": "Get request successful", "data": serializer.data}, status=status.HTTP_200_OK)
    
    def post(self, request):
        # if you want to prevent duplicate course titles per tutor:
        tutor = get_object_or_404(Tutor, user=request.user)

        serializer = CourseSerializer(data=request.data)

        if serializer.is_valid():
            # attach the tutor automatically (students cannot set this)
            serializer.save(tutor=tutor) 
            return Response({"message": "Post request successful"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id):
        try:
            course_data = Course.objects.get(id=id)
        except Course.DoesNotExist:
             return Response({"message": "This course does not exist"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = CourseSerializer(course_data, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Put request successful"}, status=status.HTTP_200_OK)
        else:
            return Response({"message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
    def patch(self, request, id):
        try:
            course_data = Course.objects.get(id=id)
        except Course.DoesNotExist:
             return Response({"message": "This tutor does not exist"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = CourseSerializer(course_data, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Patch request successful"}, status=status.HTTP_200_OK)
        else:
            return Response({"message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        try:
            course_data = Course.objects.get(id=id)
        except Course.DoesNotExist:
             return Response({"message": "This course does not exist"}, status=status.HTTP_404_NOT_FOUND)
        course_data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


class Subscribe(APIView):
    def post(self, request, id):
        # Find the course the student wants to subscribe to if it does exists in the database 
        course = get_object_or_404(Course, id=id)

        # Validate the request data to check if the student exists in the database
        serializer = SubscribeSerializer(data=request.data)

        if serializer.is_valid():
            # Get the student_id from the validated data
            student_id = serializer.validated_data['student_id']

            # Make sure this student actually exists in the database
            student = get_object_or_404(Student, id=student_id)

            # Add this student to the course's "students" list
            # The method is like append in the list
            course.students.add(student)

            return Response(
                {"message": f"Student {student.id} subscribed to course {course.id}"},
                status=status.HTTP_200_OK
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

