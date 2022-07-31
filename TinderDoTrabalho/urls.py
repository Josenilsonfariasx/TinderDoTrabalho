from django.contrib import admin
from django.urls import path, include

from usuario.models import usuario

urlpatterns = [
    path('admin/', admin.site.urls),
    path('vagas/', include('vagas.urls')),
    path('auth/', include('administracao.urls')),
    path('auth/', include('usuario.urls')),
]
