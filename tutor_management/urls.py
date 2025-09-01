from django.urls import path
from .views import TutorManagement


urlpatterns = [
    path('endpoint/', TutorManagement.as_view(), name="tutor_management"),
    path('endpoint/<int:id>/', TutorManagement.as_view(), name="tutor_management_with_id")
]