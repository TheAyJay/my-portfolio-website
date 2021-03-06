# Generated by Django 3.0.5 on 2020-04-20 08:05

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('myprojects', '0025_auto_20200417_1604'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='c_type',
            field=models.CharField(default='P', max_length=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='t_code_url',
            field=models.CharField(default='P', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='t_key_features',
            field=tinymce.models.HTMLField(default='P'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='t_objective',
            field=models.TextField(default='P'),
            preserve_default=False,
        ),
    ]
