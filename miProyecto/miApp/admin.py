from django.contrib import admin
from .models import CustomUser, Evento, Reservas, Comentario


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'rol', 'bio')
    list_filter = ('rol',)
    search_fields = ('username','email')


@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'date_time','organizador','capacidad')
    list_filter = ('date_time','organizador')
    search_fields = ('titulo', 'descripcion')

@admin.register(Reservas)
class ReservasAdmin(admin.ModelAdmin):
    list_display = ('user','evento','tickets_reservados','estado')
    list_filter = ('estado')
    search_fields = ('user__username','evento_titulo')



