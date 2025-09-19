from django.contrib import admin
from .models import Student

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "interests", "level"]
    search_fields = ["user", "interests"]


admin.site.register(Student, StudentAdmin)