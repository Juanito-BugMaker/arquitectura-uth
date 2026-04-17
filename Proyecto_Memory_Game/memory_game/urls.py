from django.urls import path
from . import views

urlpatterns = [

    # 🔐 AUTENTICACIÓN
    path('', views.login_view, name='login'),
    path('login/', views.login_view, name='login'),  # 🔥 IMPORTANTE
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),

    # 🏠 PRINCIPAL
    path('menu/', views.menu_view, name='menu'),

    # 🎮 JUEGO
    path('difficulty/', views.difficulty_view, name='difficulty'),
    path('game/', views.game_view, name='game'),
    path('save-game/', views.save_game, name='save_game'),

    # 👤 PERFIL
    path('profile/', views.profile_view, name='profile'),

    # 🏆 RANKING
    path('ranking/', views.ranking_view, name='ranking'),
]