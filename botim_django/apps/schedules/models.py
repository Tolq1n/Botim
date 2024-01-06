from django.db import models
from ..users.models import User
from parler.models import TranslatableModel, TranslatedFields


class WeekDay(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(max_length=15)
    )
    
    def __str__(self):
        return self.name
    

class DayKind(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(max_length=20)
    )
    
    def __str__(self):
        return self.name
    

class Schedule(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    weekday = models.ForeignKey(WeekDay, on_delete=models.CASCADE, help_text="Hafta kunlari POST qilish uchun id sini yuborish kerak")
    daykind = models.ForeignKey(DayKind, on_delete=models.CASCADE, help_text="Fanni har hafta, toq, juft, bo'sh qoldirish. id ")
    subject = models.CharField(max_length=150, null=True, blank=True)
    teacher = models.CharField(max_length=100, null=True, blank=True)
    lesson_type = models.CharField(max_length=100, null=True, blank=True)
    room = models.CharField(max_length=100, null=True, blank=True)
    # order_number = models.IntegerField()
    
    def __str__(self) -> str:
        return self.subject
    
    
class TimeConfig(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time1 = models.CharField(max_length=15, default="9:30-10:50")
    time2 = models.CharField(max_length=15, default="11:00-12:20")
    time3 = models.CharField(max_length=15, default="12:30-13:50")
    time4 = models.CharField(max_length=15, default="14:20-15:40")
    time5 = models.CharField(max_length=15, default="")
    time6 = models.CharField(max_length=15, default="")
    time7 = models.CharField(max_length=15, default="")




