# Generated by Django 2.2 on 2020-11-03 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_data', '0018_auto_20201103_1422'),
    ]

    operations = [
        migrations.AddField(
            model_name='tipe',
            name='qty_total',
            field=models.PositiveIntegerField(default=1, verbose_name='Total'),
        ),
        migrations.DeleteModel(
            name='StockTotal',
        ),
    ]
