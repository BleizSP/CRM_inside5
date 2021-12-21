# Generated by Django 4.0 on 2021-12-21 13:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='retention',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='retention', to='crm.employee'),
        ),
        migrations.AlterField(
            model_name='client',
            name='salesman',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='salesman', to='crm.employee'),
        ),
    ]