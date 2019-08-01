## -*- coding: utf-8 -*-
from rest_framework.views import APIView
from rest_framework.response import Response


class TaskView(APIView):
    data = [
        {"name": "enPiT"},
        {"name": "enPiT2"},
        {"name": "enPiT3"}
    ]

    def get(self, request, format=None):
        user = request.GET['username']
        age = request.GET['age']
        return Response("{}-{}".format(user, age))

    def post(self, request, format=None):
        print(request.data["id"])
        return Response(self.data[request.data["id"]])
        # return Response(self.data)
