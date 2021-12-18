# Generated by Django 4.0 on 2021-12-18 11:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Employees', '0001_initial'),
        ('Clients', '0011_remove_client_client_retention_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='client_salesman',
        ),
        migrations.AddField(
            model_name='client',
            name='client_salesman',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Employees.employees'),
            preserve_default=False,
        ),
    ]
