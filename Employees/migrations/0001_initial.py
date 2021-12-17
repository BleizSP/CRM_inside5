# Generated by Django 4.0 on 2021-12-17 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employees_name', models.CharField(max_length=20)),
                ('employees_lastname', models.CharField(max_length=20)),
                ('employees_phone', models.IntegerField()),
                ('employees_email', models.EmailField(max_length=20, null=True)),
                ('employees_rank', models.CharField(max_length=20)),
                ('employees_group', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Employee',
                'verbose_name_plural': 'Employees',
            },
        ),
    ]