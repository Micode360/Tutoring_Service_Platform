from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import StudentSerializer
from .models import Student

# Create your views here.
class StudentManagement(APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response({"message": "Get request successful", "data": serializer.data}, status=status.HTTP_200_OK)
    

    def post(self, request):
        student_data = request.data

        if Student.objects.filter(user=request.user).exists():
            return Response({"message": "A tutor profile already exists for this user. Use PATCH/PUT to update."}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = StudentSerializer(data=student_data)

        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response({"message": "Post request successful"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    

    def put(self, request, id):
        try:
            student_data = Student.objects.get(id=id)
        except Student.DoesNotExist:
             return Response({"message": "This student does not exist"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = StudentSerializer(student_data, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Put request successful"}, status=status.HTTP_200_OK)
        else:
            return Response({"message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        

    def patch(self, request, id):
        try:
            student_data = Student.objects.get(id=id)
        except Student.DoesNotExist:
             return Response({"message": "This student does not exist"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = StudentSerializer(student_data, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Patch request successful"}, status=status.HTTP_200_OK)
        else:
            return Response({"message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    
    def delete(self, request, id):
        try:
            tutor_data = Student.objects.get(id=id)
        except Student.DoesNotExist:
             return Response({"message": "This student does not exist"}, status=status.HTTP_404_NOT_FOUND)
        tutor_data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
