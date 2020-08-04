from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from task_cabinet_with_auth.models.authTask import AuthTask


class AuthTaskCreateSerializer(ModelSerializer):
    owner = serializers.ReadOnlyField(source='authuser.username')

    class Meta:
        model = AuthTask
        fields = ['owner', 'todo_name', 'todo_text', 'dead_line']
