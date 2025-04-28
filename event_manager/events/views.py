from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics, filters
from rest_framework.permissions import (AllowAny,
                                        IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)

from .models import Event, EventRegistration
from .permissions import (IsAdminOrOwner, 
                          IsOwnerOrReadOnly, 
                          PermissionByMethodMixin)
from .serializers import (EventSerializer, 
                          UserSerializer,
                          EventRegistrationSerializer)


class EventViewSet(PermissionByMethodMixin, viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permissions_map = {
            'GET': [AllowAny],
            'HEAD': [AllowAny],
            'OPTIONS': [AllowAny],
            'POST': [IsAuthenticatedOrReadOnly],
            'PUT': [IsOwnerOrReadOnly],
            'PATCH': [IsOwnerOrReadOnly],
            'DELETE': [IsAdminOrOwner],
        }

class RegistrationAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer


class EventRegistrationViewSet(PermissionByMethodMixin, viewsets.ModelViewSet):
    queryset = EventRegistration.objects.all()
    serializer_class = EventRegistrationSerializer
    permissions_map = {
            'GET': [AllowAny],
            'HEAD': [AllowAny],
            'OPTIONS': [AllowAny],
            'POST': [IsAuthenticated],
            'PUT': [IsOwnerOrReadOnly],
            'PATCH': [IsOwnerOrReadOnly],
            'DELETE': [IsAdminOrOwner],
        }

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    filter_backends = [DjangoFilterBackend, 
                       filters.SearchFilter,
                       filters.OrderingFilter]
    
    filterset_fields = ['title', 'date', 'location', 'status', 'organizer']
    search_fields = ['title', 'description', 'location', 'organizer']
    ordering_fields = ['date', 'created']
    ordering = ['date']