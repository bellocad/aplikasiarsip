# Generated by Django 3.1.7 on 2021-05-01 07:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sikept', '0020_order_jenis'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='pts',
            new_name='nama_pts',
        ),
        migrations.RenameField(
            model_name='pts',
            old_name='name',
            new_name='nama_pts',
        ),
        migrations.RenameField(
            model_name='pts',
            old_name='Provinsi',
            new_name='provinsi',
        ),
    ]