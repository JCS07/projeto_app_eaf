from django.urls import path
from apps.menu_geral.views import menu_geral

urlpatterns = [
    path('menu_geral/', menu_geral, name='menu_geral'),
]