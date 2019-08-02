from rest_framework import serializers
from task_cabinet.models.task import Task


class UserSerializer(serializers.Serializer):
    # name = serializers.CharField()
    # age = serializers.IntegerField()
    ping = serializers.CharField()
    # class Meta:
    #     model = Task
    #     fields = '__all__'