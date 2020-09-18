# Generated by Django 3.1.1 on 2020-09-16 05:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HEHE', '0011_profile_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Phone',
            field=models.CharField(blank=True, max_length=10, null=True, validators=[django.core.validators.RegexValidator('0?[5-9]{1}\\d{9}$')]),
        ),
    ]
