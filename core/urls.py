# core/urls.py

from django.urls import path
from .views import AutorListCreateView, CategoriaListCreateView, LivroListCreateView

urlpatterns = [
    path('autores/', AutorListCreateView.as_view(), name='autor-list-create'),
    path('categorias/', CategoriaListCreateView.as_view(), name='categoria-list-create'),
    path('livros/', LivroListCreateView.as_view(), name='livro-list-create'),
]
