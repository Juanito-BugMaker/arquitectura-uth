from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import PlayerStats, GameHistory
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Sum
import json


# 🔐 LOGIN
def login_view(request):
    if request.user.is_authenticated:
        return redirect('menu')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('menu')
        else:
            return render(request, 'login.html', {
                'error': 'Credenciales incorrectas'
            })

    return render(request, 'login.html')


# 📝 REGISTRO
def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {
                'error': 'Usuario ya existe'
            })

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        PlayerStats.objects.create(user=user)

        return redirect('login')

    return render(request, 'register.html')


# 🏠 MENU
@login_required(login_url='login')
def menu_view(request):
    return render(request, 'menu.html')


# 🎮 JUEGO
@login_required(login_url='login')
def game_view(request):
    level = request.GET.get('level')

    valid_levels = ['basic', 'medium', 'hard', 'extreme']

    if level not in valid_levels:
        return redirect('difficulty')

    return render(request, 'game.html', {
        'level': level
    })


# 👤 PERFIL GAMER
@login_required(login_url='login')
def profile_view(request):
    stats, _ = PlayerStats.objects.get_or_create(user=request.user)

    history = GameHistory.objects.filter(user=request.user).order_by('-created_at')[:10]

    # 🧠 WIN RATE
    total = stats.games_played
    win_rate = int((stats.wins / total) * 100) if total > 0 else 0

    return render(request, 'profile.html', {
        'stats': stats,
        'history': history,
        'win_rate': win_rate
    })


# 🏆 RANKING GLOBAL
@login_required(login_url='login')
def ranking_view(request):
    ranking = (
        PlayerStats.objects
        .select_related('user')
        .annotate(total_score=Sum('score'))
        .order_by('-total_score')[:10]
    )

    return render(request, 'ranking.html', {
        'ranking': ranking
    })


# 🚪 LOGOUT
def logout_view(request):
    logout(request)
    return redirect('login')


# 🎚️ DIFICULTAD
@login_required(login_url='login')
def difficulty_view(request):
    return render(request, 'difficulty.html')


# 💾 GUARDAR RESULTADO DEL JUEGO (🔥 MEJORADO)
@login_required(login_url='login')
def save_game(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)

            result = data.get("result")
            level = data.get("level")
            time_spent = data.get("time")

            stats, _ = PlayerStats.objects.get_or_create(user=request.user)

            # 🎯 SISTEMA DE PUNTOS
            base_points = {
                "basic": 50,
                "medium": 100,
                "hard": 200,
                "extreme": 400
            }

            score = 0
            if result == "win":
                score = base_points.get(level, 50) + max(0, 100 - time_spent)

            # 📊 ACTUALIZAR STATS
            stats.games_played += 1
            stats.score += score

            if result == "win":
                stats.wins += 1
            elif result == "lose":
                stats.losses += 1

            stats.save()

            # 📜 HISTORIAL
            GameHistory.objects.create(
                user=request.user,
                level=level,
                result=result,
                time_spent=time_spent,
                score=score
            )

            return JsonResponse({
                "status": "ok",
                "score": score
            })

        except Exception as e:
            return JsonResponse({
                "status": "error",
                "message": str(e)
            })