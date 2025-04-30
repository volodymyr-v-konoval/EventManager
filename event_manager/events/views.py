from django.core.mail import send_mail
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
from .tasks import send_registration_email



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
    
    filter_backends = [DjangoFilterBackend, 
                       filters.SearchFilter,
                       filters.OrderingFilter]
    
    filterset_fields = ['title', 'date', 'location', 'status', 'organizer']
    search_fields = ['title', 'description', 'location', 'organizer']
    ordering_fields = ['date', 'created']
    ordering = ['date']


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
        registration = serializer.save(user=self.request.user)

        send_registration_email.delay(
            user_email=registration.user.email,
            username=registration.user.username,
            event_title=registration.event.title,
            event_date=registration.event.date.strftime('%d.%m.%Y %H:%M'),
            event_location=registration.event.location,
            event_organizer=registration.event.organizer
        )
