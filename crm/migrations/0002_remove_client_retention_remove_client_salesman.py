# Generated by Django 4.0 on 2021-12-20 15:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='retention',
        ),
        migrations.RemoveField(
            model_name='client',
            name='salesman',
        ),
    ]