from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .serializers import UserSerializer
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken


# Create your views here.
class RegisterUsers(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "user registeration successful."})
        return Response({"message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class LoginUsers(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        user = authenticate(email=email, password=password)


        if user is not None:
            access = AccessToken.for_user(user)
            refresh = RefreshToken.for_user(user)

            return Response({"mesaage": "login successful.", "access": str(access), "refresh": str(refresh)})
        else:
            return Response({"error": "invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
