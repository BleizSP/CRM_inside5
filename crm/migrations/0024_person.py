# Generated by Django 4.0 on 2022-01-05 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0023_delete_typeop'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='full name')),
            ],
        ),
    ]
