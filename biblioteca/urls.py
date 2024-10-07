# biblioteca/urls.py

from django.contrib import admin
from django.urls import path, include  # include é necessário para rotas de apps

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('core.urls')),  # Certifique-se de incluir suas URLs do app core
]
