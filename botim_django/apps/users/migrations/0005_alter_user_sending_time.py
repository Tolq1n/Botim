# Generated by Django 4.2.6 on 2023-11-20 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_user_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='sending_time',
            field=models.TimeField(default='07:00'),
        ),
    ]
