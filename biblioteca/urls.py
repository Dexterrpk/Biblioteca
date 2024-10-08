# biblioteca/urls.py

from django.contrib import admin
from django.urls import path, include  # Certifique-se de que o include está importado

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('core.urls')),  # Inclua as URLs do seu app core
]
