# Generated by Django 3.1.7 on 2021-04-20 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sikept', '0005_pts_provinsi'),
    ]

    operations = [
        migrations.CreateModel(
            name='Yayasan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_yys', models.CharField(max_length=200, null=True)),
                ('phone_yys', models.CharField(max_length=200, null=True)),
                ('email_yys', models.CharField(max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Ditolak', 'Ditolak'), ('Dikirim', 'Dikirim'), ('Disimpan', 'Disimpan')], max_length=200, null=True),
        ),
    ]