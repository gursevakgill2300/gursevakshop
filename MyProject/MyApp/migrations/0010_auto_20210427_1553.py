# Generated by Django 3.2 on 2021-04-27 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0009_auto_20210427_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='first_name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='customer',
            name='last_name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='customer',
            name='password',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(default='', max_length=15),
        ),
    ]
