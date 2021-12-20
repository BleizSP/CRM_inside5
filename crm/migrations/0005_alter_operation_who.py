# Generated by Django 4.0 on 2021-12-20 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0004_operation_who'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operation',
            name='who',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ftd_employees', to='crm.employee'),
        ),
    ]