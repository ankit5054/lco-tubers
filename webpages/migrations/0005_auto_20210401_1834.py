# Generated by Django 2.2 on 2021-04-01 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0004_auto_20210401_1810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='photo',
            field=models.ImageField(upload_to='./media/slider/%Y'),
        ),
    ]
