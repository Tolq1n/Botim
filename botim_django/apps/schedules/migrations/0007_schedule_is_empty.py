# Generated by Django 4.2.6 on 2024-01-15 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0006_schedule_lesson_order_alter_schedule_daykind_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='is_empty',
            field=models.BooleanField(default=False),
        ),
    ]
