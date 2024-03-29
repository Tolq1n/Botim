# Generated by Django 4.2.6 on 2024-01-15 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0005_alter_schedule_daykind_alter_schedule_weekday'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='lesson_order',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='schedule',
            name='daykind',
            field=models.ForeignKey(help_text="Fanni har hafta, toq, juft, bo'sh qoldirish. POST qilish uchun id sini yuborish kerak", on_delete=django.db.models.deletion.CASCADE, to='schedules.daykind'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='subject',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
    ]
