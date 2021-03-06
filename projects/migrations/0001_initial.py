# Generated by Django 3.1.1 on 2020-12-06 22:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import projects.models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myadmin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image_Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_type_name', models.CharField(max_length=100, unique=True, verbose_name='Image Type Name')),
            ],
            options={
                'verbose_name': 'Image Type',
                'verbose_name_plural': 'Image Types',
                'ordering': ['image_type_name'],
            },
        ),
        migrations.CreateModel(
            name='Project_Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_name', models.CharField(max_length=200, unique=True, verbose_name='Album Name')),
                ('album_description', models.TextField(blank=True, max_length=2000, null=True)),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True)),
                ('published_album', models.BooleanField(default=False)),
                ('date_created', models.DateField(auto_now_add=True, verbose_name='date created')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='date updated')),
            ],
            options={
                'verbose_name': 'Project Album',
                'verbose_name_plural': 'Project Albums',
                'ordering': ['album_name'],
            },
        ),
        migrations.CreateModel(
            name='Project_Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Name')),
                ('category_filter', models.CharField(blank=True, max_length=255, null=True, verbose_name='Category Filter')),
                ('display', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Project Category',
                'verbose_name_plural': 'Project Categories',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Project_Feature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feature', models.CharField(max_length=255, verbose_name='Project Features')),
                ('feature_filter', models.CharField(blank=True, max_length=255, null=True, verbose_name='Feature Filter')),
                ('display', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Feature',
                'verbose_name_plural': 'Features',
            },
        ),
        migrations.CreateModel(
            name='Project_Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=100, verbose_name='Language')),
                ('language_filter', models.CharField(blank=True, max_length=255, null=True, verbose_name='Language Filter')),
                ('display', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Language',
                'verbose_name_plural': 'Languages',
                'ordering': ['language'],
            },
        ),
        migrations.CreateModel(
            name='Project_Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('summary', models.TextField(max_length=1000)),
                ('body', tinymce.models.HTMLField()),
                ('date_created', models.DateField(auto_now_add=True, verbose_name='date created')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='date updated')),
                ('published', models.BooleanField(default=False)),
                ('github', models.CharField(blank=True, max_length=255, null=True, verbose_name='GitHub')),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='written_by', to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='category_for_project', to='projects.project_category')),
                ('external_link', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='external_project_link', to='myadmin.external_link')),
                ('features', models.ManyToManyField(related_name='project_features', to='projects.Project_Feature')),
                ('languages', models.ManyToManyField(related_name='project_languages', to='projects.Project_Language')),
            ],
            options={
                'verbose_name': 'Project Post',
                'verbose_name_plural': 'Project Posts',
            },
        ),
        migrations.CreateModel(
            name='Project_Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=100, verbose_name='Status')),
                ('status_filter', models.CharField(blank=True, max_length=255, null=True, verbose_name='Status Filter')),
                ('display', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Project Status',
                'verbose_name_plural': 'Project Status',
                'ordering': ['status'],
            },
        ),
        migrations.CreateModel(
            name='Slideshow_Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=255, verbose_name='Slide Header')),
                ('paragraph', models.TextField(max_length=2000, verbose_name='Slide Paragraph')),
                ('active', models.BooleanField(default=False)),
                ('image', models.ImageField(upload_to=projects.models.pages_upload_location, verbose_name='Image')),
                ('image_alt', models.CharField(blank=True, max_length=255, null=True, verbose_name='Image Alt')),
                ('order', models.IntegerField(blank=True, default=0, null=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='projects.project_post')),
            ],
            options={
                'verbose_name': 'Slideshow Project',
                'verbose_name_plural': 'Slideshow Projects',
            },
        ),
        migrations.AddField(
            model_name='project_post',
            name='status',
            field=models.ManyToManyField(related_name='project_status', to='projects.Project_Status'),
        ),
        migrations.CreateModel(
            name='Project_Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(blank=True, default=0, null=True)),
                ('height', models.IntegerField()),
                ('width', models.IntegerField()),
                ('image', models.ImageField(height_field='height', upload_to=projects.models.upload_location, verbose_name='Image', width_field='width')),
                ('image_caption', models.CharField(blank=True, max_length=255, null=True, verbose_name='Image Caption')),
                ('default_image', models.BooleanField(default=False)),
                ('additional_text', models.TextField(blank=True, null=True, verbose_name='Additional Text')),
                ('published_image', models.BooleanField(default=False)),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True)),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='date updated')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images_in_album', to='projects.project_album')),
                ('image_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='image_type', to='projects.image_type')),
            ],
            options={
                'verbose_name': 'Project Image',
                'verbose_name_plural': 'Project Images',
                'ordering': ['album', 'order'],
            },
        ),
        migrations.AddField(
            model_name='project_album',
            name='project_name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='album_for_project', to='projects.project_post'),
        ),
        migrations.CreateModel(
            name='Current_Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=255, verbose_name='Current Header')),
                ('paragraph', models.TextField(max_length=2000, verbose_name='Current Paragraph')),
                ('active', models.BooleanField(default=False)),
                ('image', models.ImageField(upload_to=projects.models.pages_upload_location, verbose_name='Image')),
                ('image_alt', models.CharField(blank=True, max_length=255, null=True, verbose_name='Image Alt')),
                ('order', models.IntegerField(blank=True, default=0, null=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='projects.project_post')),
            ],
            options={
                'verbose_name': 'Current Project',
                'verbose_name_plural': 'Current Projects',
            },
        ),
    ]
