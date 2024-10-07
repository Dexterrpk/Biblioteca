from rest_framework import generics
from .models import Livro, Categoria, Autor
from .serializers import LivroSerializer, CategoriaSerializer, AutorSerializer
from django_filters import rest_framework as filters

class CategoriaFilter(filters.FilterSet):
    nome = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Categoria
        fields = ['nome']

class AutorFilter(filters.FilterSet):
    nome = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Autor
        fields = ['nome']

class LivroFilter(filters.FilterSet):
    titulo = filters.CharFilter(lookup_expr='icontains')
    autor = filters.CharFilter(field_name='autor__nome', lookup_expr='icontains')
    categoria = filters.CharFilter(field_name='categoria__nome', lookup_expr='icontains')

    class Meta:
        model = Livro
        fields = ['titulo', 'autor', 'categoria']

class CategoriaList(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    filterset_class = CategoriaFilter
    ordering_fields = ['nome']
    search_fields = ['^nome']

class CategoriaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class AutorList(generics.ListCreateAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    filterset_class = AutorFilter
    ordering_fields = ['nome']
    search_fields = ['^nome']

class AutorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

class LivroList(generics.ListCreateAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    filterset_class = LivroFilter
    ordering_fields = ['titulo', 'autor__nome', 'categoria__nome', 'publicado_em']
    search_fields = ['^titulo', '^autor__nome', '^categoria__nome']

class LivroDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer