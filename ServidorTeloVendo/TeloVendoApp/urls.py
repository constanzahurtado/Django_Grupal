from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('', views.index),
    path('base_cliente/', views.base_cliente),
    path('proveedor/', views.base_proveedor)
]