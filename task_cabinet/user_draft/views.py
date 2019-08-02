from task_cabinet.models.user import User
from task_cabinet.serializers.user import UserSerializer
from rest_framework.response import Response
from rest_framework import viewsets, status


class UserViewSet(viewsets.ModelViewSet):
    """
    API For UserModel
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # def list(self, request):
    #     pass
    #
    # def create(self, request):
    #     pass
    #
    # def retrieve(self, request, pk=None):
    #     pass
    #
    # def update(self, request, pk=None):
    #     pass

    # def partial_update(self, request, pk=None):
    #     pass

    # def destroy(self, request, pk=None):
    #     pass
