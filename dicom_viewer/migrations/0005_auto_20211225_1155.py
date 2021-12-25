# Generated by Django 3.2.9 on 2021-12-25 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dicom_viewer', '0004_auto_20211223_1710'),
    ]

    operations = [
        migrations.AddField(
            model_name='dicom',
            name='type',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dicom',
            name='file_jpg',
            field=models.FileField(blank=True, null=True, upload_to='dicoms/img'),
        ),
        migrations.AlterField(
            model_name='dicom',
            name='image_size',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dicom',
            name='modality',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dicom',
            name='patient_id',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dicom',
            name='patient_name',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dicom',
            name='pixel_spacing_x',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dicom',
            name='pixel_spacing_y',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dicom',
            name='sex',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dicom',
            name='slice_location',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dicom',
            name='sop_class',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dicom',
            name='study_date',
            field=models.TextField(blank=True, null=True),
        ),
    ]
