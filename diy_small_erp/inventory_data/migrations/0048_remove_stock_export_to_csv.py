# Generated by Django 2.2 on 2020-11-04 18:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_data', '0047_auto_20201104_1804'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='export_to_CSV',
        ),
    ]
