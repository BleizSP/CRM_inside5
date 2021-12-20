# Generated by Django 4.0 on 2021-12-20 15:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('type', models.CharField(max_length=20)),
                ('iban', models.CharField(blank=True, max_length=128, null=True)),
                ('wallet', models.CharField(blank=True, max_length=128, null=True)),
                ('owner', models.CharField(blank=True, max_length=64, null=True)),
                ('swift', models.CharField(blank=True, max_length=20, null=True)),
                ('country', models.CharField(blank=True, max_length=20, null=True)),
                ('adres', models.TextField(blank=True, max_length=128, null=True)),
                ('reg_date', models.DateField(blank=True, null=True)),
                ('status', models.BooleanField()),
            ],
            options={
                'verbose_name': 'Bank',
                'verbose_name_plural': 'Banks',
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('lastname', models.CharField(max_length=64)),
                ('phone', models.DecimalField(decimal_places=0, max_digits=20)),
                ('email', models.EmailField(max_length=64, null=True)),
                ('reg_time', models.DateField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Client',
                'verbose_name_plural': 'Client',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('lastname', models.CharField(max_length=64)),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=64, null=True)),
                ('rank', models.CharField(max_length=20)),
                ('group', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Employee',
                'verbose_name_plural': 'Employee',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=64)),
            ],
            options={
                'verbose_name': 'Status',
                'verbose_name_plural': 'Status',
            },
        ),
        migrations.CreateModel(
            name='Operation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cash', models.DecimalField(decimal_places=2, max_digits=12)),
                ('date', models.DateField(blank=True, null=True)),
                ('bank', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bank', to='crm.bank')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='kto', to='crm.client')),
                ('status', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='stat', to='crm.status')),
            ],
            options={
                'verbose_name': 'Operations',
                'verbose_name_plural': 'Operations',
            },
        ),
        migrations.AddField(
            model_name='client',
            name='retention',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='retention', to='crm.employee'),
        ),
        migrations.AddField(
            model_name='client',
            name='salesman',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='salesman', to='crm.employee'),
        ),
    ]
