from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Schedule
from apps.schedules.models import TimeConfig

@receiver(post_save, sender=Schedule)
def schedule_sorter(sender, instance, **kwargs):
    pass
    # Disconnect the signal temporarily
    # post_save.disconnect(schedule_sorter, sender=Schedule)

    # if instance.daykind.id == 2:
    #     Schedule.objects.create(user=instance.user, weekday_id=instance.weekday.id, daykind_id=3, subject=None, \
    #                         teacher=None, lesson_type=None, room=None, is_empty=True)

    # if instance.daykind.id == 3:
    #     Schedule.objects.create(user=instance.user, weekday_id=instance.weekday.id, daykind_id=2, subject=None, \
    #                         teacher=None, lesson_type=None, room=None, is_empty=True)

    # if instance.daykind.id == 4:
    #     instance.is_empty = True
    #     instance.save()

    # Reconnect the signal
    # post_save.connect(schedule_sorter, sender=Schedule)
