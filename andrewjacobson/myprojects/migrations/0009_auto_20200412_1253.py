# Generated by Django 3.0.5 on 2020-04-12 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myprojects', '0008_auto_20200412_1252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='t_image_path',
            field=models.FilePathField(path='myprojects/static/img'),
        ),
    ]