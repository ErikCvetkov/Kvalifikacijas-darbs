# Generated by Django 3.2.9 on 2022-01-04 20:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_remove_patient_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_superuser',
        ),
    ]