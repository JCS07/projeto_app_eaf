from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.home.urls')),
    path('', include('apps.menu_geral.urls')),
    path('', include('apps.funcionarios.urls')),
    path('', include('apps.clientes.urls')),
]