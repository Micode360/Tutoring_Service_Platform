from django.contrib import admin
from .models import Course

# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display = ["id", "tutor", "title", "description", "video_file"]
    search_fields = ["title", "tutor", "students"]


admin.site.register(Course, CourseAdmin)