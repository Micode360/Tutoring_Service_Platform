from django.contrib import admin
from .models import Tutor

# Register your models here.
class TutorAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "bio", "profile_picture"]
    search_fields = ["user", "rating"]


admin.site.register(Tutor, TutorAdmin)