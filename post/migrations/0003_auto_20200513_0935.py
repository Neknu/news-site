# Generated by Django 2.2.10 on 2020-05-13 06:35

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20200513_0932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=tinymce.models.HTMLField(verbose_name='Content'),
        ),
    ]
