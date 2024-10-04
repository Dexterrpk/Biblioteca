from rest_framework import serializers
from .models import Categoria, Autor, Livro

class CategoriaSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nome = serializers.CharField(max_length=100)

class AutorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nome = serializers.CharField(max_length=100)

class LivroSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    titulo = serializers.CharField(max_length=200)
    autor = serializers.PrimaryKeyRelatedField(queryset=Autor.objects.all())
    categoria = serializers.PrimaryKeyRelatedField(queryset=Categoria.objects.all())
    publicado_em = serializers.DateField()
