from django.contrib import admin
from .models import Teams, UserReport, Profile, ProjectReport, Projects

# Register your models here.

admin.site.register(Teams)
admin.site.register(UserReport)
admin.site.register(Profile)

