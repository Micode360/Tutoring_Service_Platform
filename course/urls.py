from django.urls import path
from .views import CourseManagement, Subscribe



urlpatterns = [
    path('endpoint/', CourseManagement.as_view(), name="course"),
    path('endpoint/<int:id>/', CourseManagement.as_view(), name="course_with_id"),
    path('subscribe/<int:id>/', Subscribe.as_view(), name="suscribe_with_id"),
]