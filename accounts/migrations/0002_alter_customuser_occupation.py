# Generated by Django 4.0.4 on 2022-10-02 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='occupation',
            field=models.CharField(choices=[('CO', 'Company'), ('SU', 'Student'), ('CJ', 'Teacher'), ('UN', 'Ohter')], default='UN', max_length=2),
        ),
    ]