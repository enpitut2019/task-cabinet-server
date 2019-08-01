from rest_framework import serializers
from .models import Calc


class ClacSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calc
        fields = ('id', 'first_number', 'second_number', 'calc')
    def get_add_result(self, instance):
        return 
