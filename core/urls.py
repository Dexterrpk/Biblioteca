from django.urls import path
from . import views

urlpatterns = [
    path('livros/', views.LivroList.as_view(), name='livro-list'),
    path('livros/<int:pk>/', views.LivroDetail.as_view(), name='livro-detail'),
    path('categorias/', views.CategoriaList.as_view(), name='categoria-list'),
    path('categorias/<int:pk>/', views.CategoriaDetail.as_view(), name='categoria-detail'),
    path('autores/', views.AutorList.as_view(), name='autor-list'),
    path('autores/<int:pk>/', views.AutorDetail.as_view(), name='autor-detail'),
]#from django.urls import path
#from . import views

#urlpatterns = [
#    path('livros/', views.livro_list_create, name='livros-list-create'),
#]


# core/urls.py

from django.urls import path
from .views import LivroList, LivroDetail

urlpatterns = [
    path('livros/', LivroList.as_view(), name='livros-list'),
    path('livros/<int:pk>/', LivroDetail.as_view(), name='livro-detail'),
]
