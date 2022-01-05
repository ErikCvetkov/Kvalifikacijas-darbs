# Generated by Django 3.2.9 on 2022-01-04 21:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0013_auto_20220104_2306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='pers_code',
            field=models.CharField(max_length=11, unique=True, validators=[django.core.validators.RegexValidator(code='nomatch', message='Length has to be 11.', regex='^.{11}$')]),
        ),
    ]
