from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PlatoSerializer, AlimentoSerializer
from .models import Plato, Alimento

# Create your views here.

class platoViewSet(viewsets.ModelViewSet):
    queryset = Plato.objects.all()
    serializer_class = PlatoSerializer

class alimentoViewSet(viewsets.ModelViewSet):
    queryset = Alimento.objects.all()
    serializer_class = AlimentoSerializer