# Generated by Django 2.2 on 2020-11-03 08:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_data', '0006_auto_20201103_0807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockin',
            name='tipe',
            field=models.ForeignKey(default=999, on_delete=django.db.models.deletion.SET_DEFAULT, to='inventory_data.Tipe', verbose_name='Nama Tipe'),
        ),
        migrations.AlterField(
            model_name='tipe',
            name='tipe',
            field=models.CharField(max_length=64, null=True, unique=True, verbose_name='Nama Tipe'),
        ),
    ]
