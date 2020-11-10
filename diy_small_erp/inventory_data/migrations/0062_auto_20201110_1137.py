# Generated by Django 2.2 on 2020-11-10 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_data', '0061_auto_20201109_2022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='issue_invoice',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Invoice Sell Out'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='receive_invoice',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='No. Invoice'),
        ),
        migrations.AlterField(
            model_name='stockhistory',
            name='receive_invoice',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='No. Invoice'),
        ),
    ]
