# Generated by Django 2.2 on 2020-11-03 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_data', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='ean',
            field=models.CharField(max_length=140, null=True, unique=True, verbose_name='EAN'),
        ),
    ]
