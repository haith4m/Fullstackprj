from django.db import models

# Create your models here.
# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def send_registration_email(sender, instance, created, **kwargs):
    if created:
        subject = 'Registration Confirmation'
        message = render_to_string('emails/registration_email.html', {'user': instance})
        send_mail(subject, message, 'your_email@example.com', [instance.email])