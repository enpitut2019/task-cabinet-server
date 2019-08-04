from task_cabinet.models.todoItemAsAuth import TodoItemAsAuth
from rest_framework import serializers


class TaskAuthAsAuthUserCreateSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='authuser.username')

    class Meta:
        model = TodoItemAsAuth
        fields = ['owner', 'todo_name', 'todo_text', 'dead_line']
