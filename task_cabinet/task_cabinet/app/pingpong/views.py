from .serializers import PingPongSerializer
from rest_framework import viewsets
from rest_framework.response import Response


class PingPongViewSet(viewsets.ViewSet):
    """
    Return "ping","pong"
    """
    def list(self, request):
        # queryset = User.objects.all()
        # serializer = UserSerializer(queryset, many=True)
        return Response("ping")
    def retrieve(self, request, pk=None):
        # queryset = User.objects.all()
        # user = get_object_or_404(queryset, pk=pk)
        # serializer = UserSerializer(user)
        return Response("pong")