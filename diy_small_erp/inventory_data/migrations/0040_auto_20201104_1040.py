# Generated by Django 2.2 on 2020-11-04 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_data', '0039_auto_20201104_0850'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='receivedstock',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='receivedstock',
            name='product',
        ),
        migrations.RemoveField(
            model_name='receivedstock',
            name='supplier',
        ),
        migrations.RemoveField(
            model_name='sellout',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='sellout',
            name='buyer',
        ),
        migrations.RemoveField(
            model_name='sellout',
            name='product',
        ),
        migrations.RemoveField(
            model_name='tipe',
            name='brand',
        ),
        migrations.DeleteModel(
            name='Brand',
        ),
        migrations.DeleteModel(
            name='Buyer',
        ),
        migrations.DeleteModel(
            name='ReceivedStock',
        ),
        migrations.DeleteModel(
            name='SellOut',
        ),
        migrations.DeleteModel(
            name='Supplier',
        ),
        migrations.DeleteModel(
            name='Tipe',
        ),
    ]
