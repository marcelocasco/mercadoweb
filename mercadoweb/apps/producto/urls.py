# apps/producto/urls.py
from django.urls import path
from . import views

#urlpatterns = [
    #path('', views.index, name='index'),
#]

urlpatterns = [
    path('', views.producto, name='apps.producto'), #llama a la funcion de views mediante el nombre
    path('limpieza', views.producto_limpieza, name='apps.producto_limpieza')
]

