# Generated by Django 4.0 on 2021-12-20 16:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0006_alter_operation_who'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operation',
            name='who',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='ftd_employees', to='crm.employee'),
            preserve_default=False,
        ),
    ]