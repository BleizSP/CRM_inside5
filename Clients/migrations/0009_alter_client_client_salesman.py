# Generated by Django 4.0 on 2021-12-18 10:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Employees', '0001_initial'),
        ('Clients', '0008_alter_client_client_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='client_salesman',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Employees.employees'),
        ),
    ]