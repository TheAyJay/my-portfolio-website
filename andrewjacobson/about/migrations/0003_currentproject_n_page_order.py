# Generated by Django 3.0.5 on 2020-05-15 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_auto_20200515_2150'),
    ]

    operations = [
        migrations.AddField(
            model_name='currentproject',
            name='n_page_order',
            field=models.SmallIntegerField(null=True),
        ),
    ]