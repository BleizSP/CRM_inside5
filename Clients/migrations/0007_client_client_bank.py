# Generated by Django 4.0 on 2021-12-16 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clients', '0006_alter_client_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='client_bank',
            field=models.CharField(max_length=15, null=True),
        ),
    ]