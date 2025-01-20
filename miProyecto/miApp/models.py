from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('Organizador','organizador'),
        ('Participante','participante'),
    ]
    rol= models.CharField(max_length=20, choices=ROLE_CHOICES)
    bio = models.TextField(blank=True, null=True)

def __str__(self):
    return self.username

class Evento(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    date_time = models.DateTimeField()
    capacidad = models.PositiveIntegerField()
    image_url = models.URLField()
    organizador = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='eventos_organizados')


def __str__(self):
    return self.titulo


class Reservas(models.Model):
    STATUS_CHOICES = [
        ('Pendiente','pendiente'),
        ('Confirmado','confirmado'),
        ('Cancelado','cancelado'),
    ]
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,related_name='reservas')
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE,related_name='reservas')
    tickets_reservados = models.PositiveIntegerField()
    estado = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pendiente')

    def __str__(self):
        return f"{self.user.username}-{self.evento.titulo} ({self.estado})"



class Comentario(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='comentarios')
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name='comentarios')
    texto = models.TextField()
    creado_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentado por {self.user.username} en {self.evento.titulo}"
