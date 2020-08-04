from django.shortcuts import render

# Create your views here.
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.mixins import LoginRequiredMixin

from task_cabinet_with_auth.models.authUser import AuthUser
from task_cabinet_with_auth.serializers.authUserSerializer import AuthUserCreateSerializer


class AuthUserCreateAPIView(CreateAPIView):
    queryset = AuthUser.objects.all()
    serializer_class = AuthUserCreateSerializer
