from .serializers import UserSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.decorators import api_view
from task_cabinet.models.task import Task


# class UserView(CreateAPIView):
#     queryset = Task.objects.all()
#     serializer_class = UserSerializer
#
#     @swagger_auto_schema(
#         operation_description="partial_update description override",
#         responses={404: 'slug not found'})
#     def post(self, request, format=None):
#         serializer = UserSerializer(data=request.GET)
#         if serializer.is_valid():
#             if serializer.data['name'] == 'ping':
#                 return Response({'result': 'pong'})
#             else:
#                 return Response({'result': "What's in your head?"})
#         else:
#             return Response({'error': serializer.errors})
class UserCreateAPIView(APIView):
    # queryset = Task.objects.all()
    serializer_class = UserSerializer

    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter('ping',
                          openapi.IN_QUERY,
                          description="please input ping",
                          type=openapi.TYPE_STRING)
    ])
    def get(self, request, format=None):
        serializer = UserSerializer(data=request.GET)
        print(serializer)
        if serializer.is_valid():
            if serializer.data['ping'] == 'ping':
                return Response({'result': 'pong'})
            else:
                return Response({'result': "What's in your head?"})
        else:
            return Response({'error': serializer.errors})