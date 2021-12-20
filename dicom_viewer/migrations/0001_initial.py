# Generated by Django 3.2.9 on 2021-12-13 13:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dicom',
            fields=[
                ('dicom_file', models.FileField(upload_to='dicoms')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='account.user')),
            ],
        ),
    ]