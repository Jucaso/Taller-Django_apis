from rest_framework import serializers
from .models import Plato, Alimento

class PlatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plato
        fields = '__all__'
        #fields = ['url', 'nombre', 'tiempoPreparacion', 'categoria', 'alimento']
        #depth=1

class AlimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alimento
        fields = '__all__'