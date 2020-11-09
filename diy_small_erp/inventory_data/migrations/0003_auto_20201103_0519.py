# Generated by Django 2.2 on 2020-11-03 05:19

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_data', '0002_auto_20201103_0420'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(null=True, unique=True, verbose_name='URL Brand')),
                ('brand', models.CharField(max_length=64, verbose_name='Nama Brand')),
            ],
            options={
                'verbose_name_plural': 'Brand',
            },
        ),
        migrations.CreateModel(
            name='StockIn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(null=True, unique=True, verbose_name='URL Tipe')),
                ('ean', models.CharField(max_length=64, unique=True, verbose_name='EAN')),
                ('tipe', models.CharField(max_length=64, unique=True, verbose_name='Nama Tipe')),
                ('qty_in', models.PositiveIntegerField(default=1, verbose_name='Jumlah Masuk')),
                ('date_in', models.DateField(default=django.utils.timezone.now, null=True)),
                ('brand', models.ForeignKey(default=999, on_delete=django.db.models.deletion.SET_DEFAULT, to='inventory_data.Brand', verbose_name='Nama Brand')),
            ],
            options={
                'verbose_name_plural': 'Barang Masuk',
            },
        ),
        migrations.DeleteModel(
            name='Stock',
        ),
    ]
