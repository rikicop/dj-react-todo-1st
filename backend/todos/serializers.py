# todos/serializers.py
from rest_framework import serializers
from .models import Todo, Constante

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'body',)


class ConstanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Constante
        fields = ('valor', 'descripcion')
