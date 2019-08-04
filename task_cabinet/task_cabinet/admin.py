from django.contrib import admin

from task_cabinet.models import Task, User
from task_cabinet.models import AuthUser
from .models.todoItemAsAuth import TodoItemAsAuth
from django.contrib.auth.admin import UserAdmin

admin.site.register(Task)
admin.site.register(User)
admin.site.register(AuthUser, UserAdmin)
admin.site.register(TodoItemAsAuth)