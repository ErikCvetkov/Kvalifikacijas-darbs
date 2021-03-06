# Generated by Django 3.2.9 on 2022-01-03 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dicom_viewer', '0007_dicom_medical_verdict'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dicom',
            name='status',
            field=models.CharField(choices=[('None', 'None'), ('Uploaded', 'Uploaded'), ('Broken', 'Broken'), ('In work', 'In work'), ('Checked', 'Checked'), ('Finished', 'Finished')], max_length=20),
        ),
    ]
