from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from task_cabinet_with_auth.models.authUser import AuthUser


class AuthUserCreateSerializer(ModelSerializer):
    class Meta:
        model = AuthUser
        fields = ['username', 'email', 'password']
