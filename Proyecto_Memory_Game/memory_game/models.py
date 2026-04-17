from django.db import models
from django.contrib.auth.models import User


# 🔹 Estadísticas del jugador (PERFIL GAMER)
class PlayerStats(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)
    games_played = models.IntegerField(default=0)

    # 🔥 NUEVO → SISTEMA DE PUNTOS
    score = models.IntegerField(default=0)

    def win_rate(self):
        if self.games_played == 0:
            return 0
        return int((self.wins / self.games_played) * 100)

    def __str__(self):
        return self.user.username


# 🔹 Historial de partidas
class GameHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    level = models.CharField(max_length=20)
    result = models.CharField(max_length=10)

    time_spent = models.FloatField()

    # 🔥 NUEVO → PUNTOS POR PARTIDA
    score = models.IntegerField(default=0)

    # 🔥 MEJOR NOMBRE (para ordenar bien)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.result} - {self.score} pts"