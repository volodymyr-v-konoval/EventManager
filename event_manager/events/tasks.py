from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_registration_email(user_email, 
                            username, 
                            event_title, 
                            event_date,
                            event_location,
                            event_organizer):
    subject = f'Registration confirmation for "{event_title}"'
    message = f'''Hello, {username}!

                You have successfully registered for the event:
                Title: {event_title}
                Organizer: {event_organizer}
                Date & Time: {event_date}
                Location: {event_location}

                Thank you for choosing our service!'''

    send_mail(
        subject=subject,
        message=message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[user_email],
        fail_silently=False,
    )
