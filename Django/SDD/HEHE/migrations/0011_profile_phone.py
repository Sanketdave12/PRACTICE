# Generated by Django 3.1.1 on 2020-09-16 04:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HEHE', '0010_auto_20200916_1000'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='Phone',
            field=models.CharField(blank=True, max_length=10, null=True, validators=[django.core.validators.RegexValidator('0?[5-9]{1}\\D{9}$')]),
        ),
    ]
