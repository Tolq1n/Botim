# Generated by Django 4.2.6 on 2023-10-15 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='genereted_key',
            field=models.CharField(blank=True, max_length=15, null=True, unique=True),
        ),
    ]
