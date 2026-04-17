from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),  # <-- NUEVO: Rutas mágicas de Google
    path('', include('memory_game.urls')),
]
