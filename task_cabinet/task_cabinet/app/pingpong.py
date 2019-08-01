## -*- coding: utf-8 -*-
from rest_framework.views import APIView
from rest_framework.response import Response


class TaskView(APIView):
    def get(self, request, format=None):
        user = request.GET['username']
        age = request.GET['age']
        return Response("{}-{}".format(user, age))
