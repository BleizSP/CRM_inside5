# Generated by Django 4.0 on 2021-12-18 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clients', '0012_remove_client_client_salesman_client_client_salesman'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='client_retention',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]