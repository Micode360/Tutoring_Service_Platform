from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import TutorSerializer
from .models import Tutor

# Create your views here.
class TutorManagement(APIView):
    def get(self, request):
        tutors = Tutor.objects.all()
        serializer = TutorSerializer(tutors, many=True)
        return Response({"message": "Get request successful", "data": serializer.data}, status=status.HTTP_200_OK)
    
    def post(self, request):
        tutor_data = request.data

        if Tutor.objects.filter(user=request.user).exists(): # update here
            return Response({"message": "A tutor profile already exists for this user. Use PATCH/PUT to update."}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = TutorSerializer(data=tutor_data)

        if serializer.is_valid():
            serializer.save(user=request.user) 
            return Response({"message": "Post request successful"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id):
        try:
            tutor_data = Tutor.objects.get(id=id)
        except Tutor.DoesNotExist:
             return Response({"message": "This tutor does not exist"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = TutorSerializer(tutor_data, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Put request successful"}, status=status.HTTP_200_OK)
        else:
            return Response({"message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
    def patch(self, request, id):
        try:
            tutor_data = Tutor.objects.get(id=id)
        except Tutor.DoesNotExist:
             return Response({"message": "This tutor does not exist"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = TutorSerializer(tutor_data, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Patch request successful"}, status=status.HTTP_200_OK)
        else:
            return Response({"message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        try:
            tutor_data = Tutor.objects.get(id=id)
        except Tutor.DoesNotExist:
             return Response({"message": "This tutor does not exist"}, status=status.HTTP_404_NOT_FOUND)
        tutor_data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
