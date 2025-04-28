from django.conf import settings
from django.db import models


class Event(models.Model):

    class Status(models.TextChoices):
        ONLINE = 'ON', 'Online'
        OFFLINE = 'OF', 'Offline'

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='users_events'
        )
    description = models.TextField(blank=True)
    date = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=250)
    organizer = models.CharField(max_length=250)
    status = models.CharField(
        max_length=2,
        choices=Status,
        default=Status.OFFLINE
    )

    class Meta:
        ordering = ['-date']
        indexes = [
            models.Index(fields=['-date']),
        ]

    def __str__(self):
        return self.title
