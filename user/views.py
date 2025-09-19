import random
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User, PasswordReset
from rest_framework import permissions
from .serializers import UserSerializer
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from drf_spectacular.utils import extend_schema, OpenApiExample

# Create your views here.
@extend_schema(
    summary="To register user",
    request=dict,
    responses={200:dict, 400:dict, 201: dict},
    examples= [
        OpenApiExample(
            name="Reister User",
            value={
                "first_name": "Joe",
                "last_name": "Hart",
                "email": "joehart@mail.com",
                "password": "#Limpoaitw43",
                "confirm_password": "#Limpoaitw43",
                "role": "tutor"
            }

        )
    ]
)
class RegisterUsers(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "user registeration successful."}, status=status.HTTP_201_CREATED)
        return Response({"message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@extend_schema(
    summary="To Login user",
    request=dict,
    responses={200:dict, 400:dict},
    examples= [
        OpenApiExample(
            name="Login User",
            value={
                "email": "joehart@mail.com",
                "password": "#Limpoaitw43",
            }

        )
    ]
)
class LoginUsers(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        email = request.data.get("email")
        password = request.data.get("password")

        user = authenticate(email=email, password=password)


        if user is not None:
            access = AccessToken.for_user(user)
            refresh = RefreshToken.for_user(user)

            return Response({"mesaage": "login successful.", "access": str(access), "refresh": str(refresh)})
        else:
            return Response({"error": "invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)



class ForgotPassword(APIView):
    def post(self, request):
        email = request.data.get("email")
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=404)

        # Generate your otp here
        otp = str(random.randint(100000, 999999))

        PasswordReset.objects.create(user=user, otp=otp)
        return Response({"message": "OTP sent to your email."})
    

class VerifyOTP(APIView):
    def post(self, request):
        email = request.data.get("email")
        otp = request.data.get("otp")

        try:
            user = User.objects.get(email=email)
            reset = PasswordReset.objects.filter(user=user, otp=otp, is_used=False).last()
            if reset:
                reset.is_used = True
                reset.save()
                return Response({"message": "OTP verified. You can reset your password."})
            else:
                return Response({"error": "Invalid or expired OTP"}, status=400)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=404)