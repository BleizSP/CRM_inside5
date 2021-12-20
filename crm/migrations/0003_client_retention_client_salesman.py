# Generated by Django 4.0 on 2021-12-20 15:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0002_remove_client_retention_remove_client_salesman'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='retention',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='retention', to='crm.employee'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='client',
            name='salesman',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='salesman', to='crm.employee'),
            preserve_default=False,
        ),
    ]
