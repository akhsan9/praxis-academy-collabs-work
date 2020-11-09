# Generated by Django 2.2 on 2020-11-03 07:49

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_data', '0003_auto_20201103_0519'),
    ]

    operations = [
        migrations.CreateModel(
            name='StockOut',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_in', models.DateField(default=django.utils.timezone.now, null=True)),
                ('brand', models.ForeignKey(default=999, on_delete=django.db.models.deletion.SET_DEFAULT, to='inventory_data.Brand', verbose_name='Nama Brand')),
                ('ean', models.ForeignKey(default=999, on_delete=django.db.models.deletion.SET_DEFAULT, to='inventory_data.StockIn', verbose_name='EAN')),
                ('tipe', models.ForeignKey(default=999, on_delete=django.db.models.deletion.SET_DEFAULT, to='inventory_data.StockOut', verbose_name='Nama Tipe')),
            ],
            options={
                'verbose_name_plural': 'Barang Keluar',
            },
        ),
    ]
