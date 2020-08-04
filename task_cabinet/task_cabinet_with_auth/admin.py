from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from .models.authUser import AuthUser
from .models.authTask import AuthTask

admin.site.register(AuthUser, UserAdmin)
admin.site.register(AuthTask)
