# Generated by Django 4.0.4 on 2022-10-14 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_customuser_occupation'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='user_image',
            field=models.ImageField(default='media/user-profile.png', upload_to=''),
        ),
    ]
