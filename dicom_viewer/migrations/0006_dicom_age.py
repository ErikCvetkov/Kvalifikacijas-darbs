# Generated by Django 3.2.9 on 2021-12-25 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dicom_viewer', '0005_auto_20211225_1155'),
    ]

    operations = [
        migrations.AddField(
            model_name='dicom',
            name='age',
            field=models.TextField(blank=True, null=True),
        ),
    ]
