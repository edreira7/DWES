from rest_framework import generics, permissions
from .models import Evento
from .serializers import EventSerializer
from rest_framework.pagination import PageNumberPagination

class EventPagination(PageNumberPagination):
    page_size = 5

class EventListCreateView(generics.ListCreateAPIView):
    queryset = Evento.objects.all().order_by('-fecha_hora')
    serializer_class = EventSerializer
    pagination_class = EventPagination

    def get_queryset(self):
        queryset = super().get_queryset()

        titulo = self.request.query_params.get('titulo', None)
        fecha = self.request.query_params.get('fecha', None)
        if titulo:
            queryset = queryset.filter(titulo__icontains=titulo)
        if fecha:
            queryset = queryset.filter(fecha_hora__date=fecha)
        return queryset

    def perform_create(self, serializer):
        # Verifica si el usuario es organizador antes de permitir crear un evento
        if self.request.user.is_authenticated and self.request.user.is_organizador:
            serializer.save(organizador=self.request.user)
        else:
            raise permissions.PermissionDenied("Solo los organizadores pueden crear eventos.")

# Detalle, actualización y eliminación de eventos
class EventDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Evento.objects.all()
    serializer_class = EventSerializer

    def perform_update(self, serializer):
        # Solo el organizador del evento puede actualizarlo
        evento = self.get_object()
        if self.request.user == evento.organizador:
            serializer.save()
        else:
            raise permissions.PermissionDenied("Solo el organizador puede actualizar este evento.")

    def perform_destroy(self, instance):
        # Solo el organizador del evento puede eliminarlo
        if self.request.user == instance.organizador:
            instance.delete()
        else:
            raise permissions.PermissionDenied("Solo el organizador puede eliminar este evento.")

