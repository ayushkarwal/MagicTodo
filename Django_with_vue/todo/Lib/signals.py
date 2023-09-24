from django.db.models.signals import post_save, pre_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.conf import settings
from django.core.mail import send_mail

@receiver(post_save, sender = User)
def send_alert_on_user_creation(sender, instance, created, **kwargs):
    # import pdb;pdb.set_trace()
    subject = 'Welcome'
    message = 'Test mail'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [instance.email, ]
    # send_mail( subject, message, email_from, recipient_list )