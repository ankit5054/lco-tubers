# Generated by Django 2.2 on 2021-04-01 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0002_auto_20210401_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='photo',
            field=models.ImageField(upload_to='media/slider/'),
        ),
    ]
