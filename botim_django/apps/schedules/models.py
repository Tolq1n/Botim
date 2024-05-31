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
    user = models.ForeignKey(User, on_delete=models.CASCADE, help_text="Telegram ID")
    weekday = models.ForeignKey(WeekDay, on_delete=models.CASCADE, help_text="Hafta kunlari POST qilish uchun ID sini yuborish kerak")
    daykind = models.ForeignKey(DayKind, on_delete=models.CASCADE, help_text="Fanni har hafta, toq, juft, bo'sh qoldirish. POST qilish uchun ID sini yuborish kerak")
    subject = models.CharField(max_length=150, null=True, blank=True, help_text="Har hafta, Toq hafta, Juft hafta uchun bu maydon majburiy. Bo'sh qoldirish uchun majburiy emas. string")
    teacher = models.CharField(max_length=100, null=True, blank=True, help_text="string")
    lesson_type = models.CharField(max_length=100, null=True, blank=True, help_text="string")
    room = models.CharField(max_length=100, null=True, blank=True, help_text="string")
    lesson_order = models.PositiveIntegerField(null=True, blank=True, help_text="yuborish kerak emas")
    is_empty = models.BooleanField(default=False)

    def __str__(self) -> str:
        return str(self.user.id)


class TimeConfig(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    time1 = models.CharField(max_length=15, default="9:30-10:50")
    time2 = models.CharField(max_length=15, default="11:00-12:20")
    time3 = models.CharField(max_length=15, default="12:30-13:50")
    time4 = models.CharField(max_length=15, default="14:20-15:40")
    time5 = models.CharField(max_length=15, default="")
    time6 = models.CharField(max_length=15, default="")
    time7 = models.CharField(max_length=15, default="")




