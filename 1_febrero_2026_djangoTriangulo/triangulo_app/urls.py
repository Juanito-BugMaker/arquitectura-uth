from django.urls import path
from .views import calcular_triangulo

urlpatterns = [
    path('', calcular_triangulo, name="triangulo"),
]
