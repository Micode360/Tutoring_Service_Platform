from django.urls import path
from .views import RegisterUsers, LoginUsers

urlpatterns = [
    path('register/', RegisterUsers.as_view(), name="register"),
    path('login/', LoginUsers.as_view(), name="login")
]