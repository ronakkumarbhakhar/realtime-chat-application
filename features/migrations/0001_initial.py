# Generated by Django 4.0.4 on 2022-10-11 01:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Friends',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accepted', models.BooleanField(default=False)),
                ('sent_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='frnd_rqst_sent', to=settings.AUTH_USER_MODEL)),
                ('sent_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='frnd_rqst_received', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
