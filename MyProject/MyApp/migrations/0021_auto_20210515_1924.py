# Generated by Django 3.2 on 2021-05-15 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0020_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(default='', max_length=80),
        ),
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.IntegerField(default=1),
        ),
    ]
