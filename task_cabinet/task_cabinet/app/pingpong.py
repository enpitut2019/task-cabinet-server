## -*- coding: utf-8 -*-
from rest_framework.views import APIView
from rest_framework.response import Response


class TaskGet(APIView):
    def get(self, request, format=None):
        return Response("pong")