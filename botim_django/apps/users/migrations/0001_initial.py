# Generated by Django 4.2.6 on 2023-10-15 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigIntegerField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('full_name', models.CharField(blank=True, max_length=50, null=True)),
                ('genereted_key', models.CharField(max_length=15, unique=True)),
                ('sending_time', models.TimeField(blank=True, null=True)),
                ('joined_at', models.DateTimeField(auto_now_add=True)),
                ('username', models.CharField(max_length=50)),
                ('mute', models.BooleanField(default=False)),
            ],
        ),
    ]
