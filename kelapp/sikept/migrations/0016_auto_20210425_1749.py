# Generated by Django 3.1.7 on 2021-04-25 09:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sikept', '0015_auto_20210425_1618'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='nomor',
            new_name='dokumen',
        ),
    ]
