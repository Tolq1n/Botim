from django.db import models




class User(models.Model):
    id = models.BigIntegerField(unique=True, primary_key=True)
    genereted_key = models.CharField(max_length=15, unique=True, null=True, blank=True)
    full_name = models.CharField(max_length=50, null=True, blank=True)
    sending_time = models.TimeField(default='07:00')
    joined_at = models.DateTimeField(auto_now_add=True)
    language = models.CharField(max_length=4, default='ru')
    username = models.CharField(max_length=50)
    mute = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.full_name if self.full_name is not None else self.username 
