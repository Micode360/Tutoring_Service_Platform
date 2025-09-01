from django.urls import path
from .views import CourseManagement



urlpatterns = [
    path('endpoint/', CourseManagement.as_view(), name="course"),
    path('endpoint/<int:id>/', CourseManagement.as_view(), name="course_with_id")
]