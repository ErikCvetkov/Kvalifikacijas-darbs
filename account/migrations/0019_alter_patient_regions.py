# Generated by Django 3.2.9 on 2022-01-06 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0018_auto_20220106_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='regions',
            field=models.CharField(default='None', max_length=100, null=True),
        ),
    ]