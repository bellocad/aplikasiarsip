# Generated by Django 3.1.7 on 2021-04-25 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sikept', '0013_auto_20210425_1614'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='nomor',
            new_name='dokumen',
        ),
        migrations.AlterField(
            model_name='dokumen',
            name='tanggal_surat',
            field=models.DateField(null=True, verbose_name='Tanggal Surat'),
        ),
    ]
