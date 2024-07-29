# Generated by Django 5.0.7 on 2024-07-24 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='subscription_duration',
            field=models.PositiveIntegerField(blank=True, choices=[(1, '1 месяц'), (3, '3 месяца'), (6, '6 месяцев')], null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='subscription_start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
