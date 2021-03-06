# Generated by Django 2.2 on 2020-11-04 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_data', '0042_auto_20201104_1459'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='phone_number',
        ),
        migrations.AddField(
            model_name='stock',
            name='ean',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Product ID'),
        ),
        migrations.AddField(
            model_name='stock',
            name='supplier',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Supplier'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='brand',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Brand'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='issue_by',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Warehouse Admin'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='issue_quantity',
            field=models.IntegerField(blank=True, default='0', null=True, verbose_name='Sell Out Quantity'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='issue_to',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Buyer'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='item_name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Product ID'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='quantity',
            field=models.IntegerField(blank=True, default='0', null=True, verbose_name='Total Quantity'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='receive_by',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Warehouse Admin'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='receive_quantity',
            field=models.IntegerField(blank=True, default='0', null=True, verbose_name='Received Quantity'),
        ),
    ]
