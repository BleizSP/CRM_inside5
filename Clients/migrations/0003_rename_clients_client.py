# Generated by Django 4.0 on 2021-12-16 11:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Clients', '0002_rename_client_clients'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Clients',
            new_name='Client',
        ),
    ]
