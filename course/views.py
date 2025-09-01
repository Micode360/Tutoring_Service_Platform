from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CourseSerializer
from .models import Course

# Create your views here.
class CourseSerializer(APIView):
    def get(self, request):
        courses = Course.objects.all().values()
        serializer = CourseSerializer(courses, many=True)
        return Response({"message": "Get request successful", "data": serializer.data}, status=status.HTTP_200_OK)
    
    def post(self, request):
        course_data = request.data

        if Course.objects.filter(user=request.user).exists(): # update here
            return Response({"message": "A courses profile already exists for this user. Use PATCH/PUT to update."}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = CourseSerializer(data=course_data)

        if serializer.is_valid():
            serializer.save(**{"user": request.user}) # update here
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
