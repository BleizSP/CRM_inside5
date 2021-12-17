# Generated by Django 4.0 on 2021-12-16 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Operation', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='operation',
            options={'verbose_name': 'Operation', 'verbose_name_plural': 'Operations'},
        ),
        migrations.RenameField(
            model_name='operation',
            old_name='client_cash',
            new_name='operation_client_cash',
        ),
        migrations.RenameField(
            model_name='operation',
            old_name='client_name2',
            new_name='operation_client_id',
        ),
        migrations.AddField(
            model_name='operation',
            name='operation_bank',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='operation',
            name='operation_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
