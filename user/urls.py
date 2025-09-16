from django.urls import path
from .views import RegisterUsers, LoginUsers, ForgotPassword, VerifyOTP

urlpatterns = [
    path('register/', RegisterUsers.as_view(), name="register"),
    path('login/', LoginUsers.as_view(), name="login"),
    path('forgotpassword/', ForgotPassword.as_view(), name='forgotpassword'),
    path('verifyotp/', VerifyOTP.as_view(), name="verifyotp")
]