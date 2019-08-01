from .models import Calc
from .serializers import ClacSerializer

from rest_framework import viewsets


class ClacViewSet(viewsets.ModelViewSet):
    queryset = Calc.objects.all()
    serializer_class = ClacSerializer
