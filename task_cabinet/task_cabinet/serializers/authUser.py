from task_cabinet.models import AuthUser
from rest_framework import serializers


class TaskAuthUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUser
        fields = ['username', 'email', 'password']