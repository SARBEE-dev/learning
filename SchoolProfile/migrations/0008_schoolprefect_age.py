# Generated by Django 3.1.7 on 2021-09-12 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SchoolProfile', '0007_schoolprefect'),
    ]

    operations = [
        migrations.AddField(
            model_name='schoolprefect',
            name='Age',
            field=models.IntegerField(default=10),
        ),
    ]
