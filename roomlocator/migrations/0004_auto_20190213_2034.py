# Generated by Django 2.1.5 on 2019-02-13 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roomlocator', '0003_auto_20190212_2230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roomnumber',
            name='number',
            field=models.CharField(max_length=6),
        ),
    ]
