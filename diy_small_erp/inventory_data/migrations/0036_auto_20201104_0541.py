# Generated by Django 2.2 on 2020-11-04 05:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_data', '0035_auto_20201104_0536'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brand',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='tipe',
            name='slug',
        ),
    ]
