from django.urls import path
from .views import StudentManagement


urlpatterns = [
    path('endpoint/', StudentManagement.as_view(), name="student_management"),
    path('endpoint/<int:id>/', StudentManagement.as_view(), name="student_management_with_id")
]