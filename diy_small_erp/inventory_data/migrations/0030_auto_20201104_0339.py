# Generated by Django 2.2 on 2020-11-04 03:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_data', '0029_receivedstock_admin_pass'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sellout',
            name='tipe',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory_data.Tipe', verbose_name='Tipe Barang'),
        ),
    ]
