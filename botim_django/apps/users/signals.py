from django.db.models.signals import  pre_save, post_save
from django.dispatch import receiver
from .models import User
from apps.schedules.models import TimeConfig


@receiver(post_save, sender=User)
def time_create(sender, instance, **kwargs):
    t_conf = TimeConfig.objects.create(user_id=instance.pk)
    t_conf.save()
