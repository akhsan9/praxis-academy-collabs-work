# Generated by Django 2.2 on 2020-11-10 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_data_store_b', '0003_auto_20201107_1512'),
    ]

    operations = [
        migrations.CreateModel(
            name='StockHistoryStoreB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, null=True, verbose_name='URL Product')),
                ('brand', models.CharField(blank=True, max_length=50, null=True, verbose_name='Brand')),
                ('ean', models.CharField(blank=True, max_length=50, null=True, verbose_name='Product ID')),
                ('item_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Product Name')),
                ('quantity', models.IntegerField(blank=True, default='0', null=True, verbose_name='Total Quantity')),
                ('supplier', models.CharField(blank=True, max_length=50, null=True, verbose_name='Supplier')),
                ('receive_invoice', models.CharField(blank=True, max_length=50, null=True, verbose_name='No. Invoice')),
                ('receive_quantity', models.IntegerField(blank=True, default='0', null=True, verbose_name='Received Quantity')),
                ('receive_by', models.CharField(blank=True, max_length=50, null=True, verbose_name='Warehouse Admin')),
                ('issue_to', models.CharField(blank=True, max_length=50, null=True, verbose_name='Buyer')),
                ('issue_invoice', models.CharField(blank=True, max_length=50, null=True, verbose_name='Invoice Sell Out')),
                ('issue_quantity', models.IntegerField(blank=True, default='0', null=True, verbose_name='Sell Out Quantity')),
                ('issue_by', models.CharField(blank=True, max_length=50, null=True, verbose_name='Warehouse Admin')),
                ('reorder_level', models.IntegerField(blank=True, default='0', null=True)),
                ('date_added', models.DateTimeField(null=True)),
                ('last_updated', models.DateTimeField(null=True)),
            ],
            options={
                'verbose_name_plural': 'Stock History Store B',
            },
        ),
        migrations.RemoveField(
            model_name='stockstoreb',
            name='created_by',
        ),
        migrations.AddField(
            model_name='stockstoreb',
            name='issue_invoice',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Invoice Sell Out'),
        ),
        migrations.AddField(
            model_name='stockstoreb',
            name='receive_invoice',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='No. Invoice'),
        ),
    ]
