from rest_framework import viewsets, generics
from rest_framework.permissions import (AllowAny,
                                        IsAuthenticated,
                                        IsAdminUser,
                                        IsAuthenticatedOrReadOnly)

from .models import Event
from .permissions import (IsAdminOrReadOnly, 
                          IsOwnerOrReadOnly, 
                          PermissionByMethodMixin)
from .serializers import EventSerializer, UserSerializer


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
            'DELETE': [IsAdminUser],
        }

class RegistrationAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer