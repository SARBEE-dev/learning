# Generated by Django 3.1.7 on 2021-08-27 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_auto_20210825_1803'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
