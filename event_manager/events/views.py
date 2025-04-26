from django.shortcuts import render
from rest_framework import generics

from .models import Event
from .serializers import EventSerializer


class EventAPIView(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
