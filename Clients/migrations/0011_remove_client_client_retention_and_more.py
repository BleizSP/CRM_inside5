# Generated by Django 4.0 on 2021-12-18 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employees', '0001_initial'),
        ('Clients', '0010_client_client_retention'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='client_retention',
        ),
        migrations.RemoveField(
            model_name='client',
            name='client_salesman',
        ),
        migrations.AddField(
            model_name='client',
            name='client_salesman',
            field=models.ManyToManyField(to='Employees.Employees'),
        ),
    ]