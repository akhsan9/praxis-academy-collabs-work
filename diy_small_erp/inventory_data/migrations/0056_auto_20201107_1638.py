# Generated by Django 2.2 on 2020-11-07 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_data', '0055_auto_20201107_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockhistory',
            name='slug',
            field=models.SlugField(blank=True, null=True, verbose_name='URL Product'),
        ),
    ]
