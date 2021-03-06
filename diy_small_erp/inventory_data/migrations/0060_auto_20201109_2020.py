# Generated by Django 2.2 on 2020-11-09 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_data', '0059_remove_stock_created_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='issue_invoice',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Supplier'),
        ),
        migrations.AddField(
            model_name='stock',
            name='receive_invoice',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Supplier'),
        ),
        migrations.AddField(
            model_name='stockhistory',
            name='issue_invoice',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Supplier'),
        ),
        migrations.AddField(
            model_name='stockhistory',
            name='receive_invoice',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Supplier'),
        ),
    ]
