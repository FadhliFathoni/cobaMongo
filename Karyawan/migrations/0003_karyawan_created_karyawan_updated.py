# Generated by Django 4.1.1 on 2023-02-02 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Karyawan', '0002_alter_karyawan_nama'),
    ]

    operations = [
        migrations.AddField(
            model_name='karyawan',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='karyawan',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]