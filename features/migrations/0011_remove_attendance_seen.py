# Generated by Django 4.2.1 on 2023-05-24 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0010_attendance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendance',
            name='seen',
        ),
    ]