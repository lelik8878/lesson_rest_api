
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Sun


@receiver(post_save, sender=Sun)
def send_message_johan(sender, instance, created, **kwargs):
    print(instance.__dict__)
    print('+++++Our signal+++++++++')
