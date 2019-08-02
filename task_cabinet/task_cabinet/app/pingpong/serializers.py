from rest_framework import serializers


class PingPongSerializer(serializers.Serializer):
    message = serializers.EmailField()