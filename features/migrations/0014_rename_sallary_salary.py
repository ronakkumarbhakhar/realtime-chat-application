# Generated by Django 4.2.1 on 2023-05-24 20:14

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('features', '0013_sallary'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='sallary',
            new_name='salary',
        ),
    ]