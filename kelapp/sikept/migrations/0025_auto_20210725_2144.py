# Generated by Django 3.1.7 on 2021-07-25 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sikept', '0024_auto_20210721_0905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='Jenis',
            field=models.CharField(choices=[('Akta', 'Akta'), ('SK Menkumham', 'SK Menkumham'), ('SK', 'SK'), ('Rekomendasi', 'Rekomendasi'), ('Surat', 'Surat'), ('Berita Acara', 'Berita Acara')], max_length=200, null=True),
        ),
    ]
