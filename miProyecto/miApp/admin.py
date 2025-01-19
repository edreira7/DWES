from django.contrib import admin
from .models import CustomUser, Evento, Reservas, Comentario


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'rol', 'bio')
    list_filter = ('rol',)
    search_fields = ('username','email')

