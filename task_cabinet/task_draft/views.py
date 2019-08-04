from task_cabinet.serializers import TaskSerializer
from task_cabinet.models import Task
from rest_framework.response import Response
from rest_framework import viewsets, status


class TaskViewSet(viewsets.ModelViewSet):
    """
    API For TaskModel
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def list(self, request):
        serializer = TaskSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = TaskSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        result = serializer.save()
        new_task = TaskSerializer(result)
        print(new_task.data)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        task = Task.objects.filter(id=pk).first()
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    # def update(self, request, pk=None):
    #     pass

    # def partial_update(self, request, pk=None):
    #     pass

    # def destroy(self, request, pk=None):
    #     pass
