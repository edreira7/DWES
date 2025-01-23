from rest_framework import serializers
from .models import Evento

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = '__all__'
