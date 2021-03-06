# Generated by Django 3.1.1 on 2020-12-07 09:13

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='current_project',
            name='paragraph',
            field=tinymce.models.HTMLField(max_length=2000, verbose_name='Current Paragraph'),
        ),
        migrations.AlterField(
            model_name='slideshow_project',
            name='paragraph',
            field=tinymce.models.HTMLField(max_length=2000, verbose_name='Slide Paragraph'),
        ),
    ]
