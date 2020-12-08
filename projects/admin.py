from django.contrib import admin
from projects.models import Project_Language
from projects.models import Project_Category
from projects.models import Project_Album
from projects.models import Project_Image
from projects.models import Project_Post
from projects.models import Image_Type
from projects.models import Project_Status
from projects.models import Project_Feature
from projects.models import Slideshow_Project
from projects.models import Current_Project
# from projects.models import Post

# Register your models here.
class Slideshow_Project_Admin(admin.ModelAdmin):
	list_display = ('header', 'project', 'order', 'paragraph', 'active')
	search_fields = ('title',)
	readonly_fields=()

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()	

admin.site.register(Slideshow_Project, Slideshow_Project_Admin)

class Current_Project_Admin(admin.ModelAdmin):
	list_display = ('header', 'project', 'order', 'paragraph', 'active')
	search_fields = ('title',)
	readonly_fields=()

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()	

admin.site.register(Current_Project, Current_Project_Admin)

class Project_Status_Admin(admin.ModelAdmin):
	list_display = ('status','status_filter', 'display')
	search_fields = ('status',)
	readonly_fields=()

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()	

admin.site.register(Project_Status, Project_Status_Admin)

class Project_Feature_Admin(admin.ModelAdmin):
	list_display = ('feature', 'feature_filter', 'display')
	search_fields = ('feature',)
	readonly_fields=()

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()	

admin.site.register(Project_Feature, Project_Feature_Admin)

class Project_Language_Admin(admin.ModelAdmin):
	list_display = ('language','language_filter', 'display')
	search_fields = ('language',)
	readonly_fields=()

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()	

admin.site.register(Project_Language, Project_Language_Admin)


class Project_Category_Admin(admin.ModelAdmin):
	list_display = ('name','category_filter', 'display')
	search_fields = ('name',)
	readonly_fields=()

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()	
	
admin.site.register(Project_Category, Project_Category_Admin)

class Project_Album_Admin(admin.ModelAdmin):
	list_display = ('album_name','project_name', 'published_album')
	search_fields = ('album_name',)
	readonly_fields=()

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()	
	
admin.site.register(Project_Album, Project_Album_Admin)

class Project_Image_Admin(admin.ModelAdmin):
	list_display = ('image_caption', 'slug', 'image_type', 'image', 'order', 'default_image', 'published_image', 'album')
	search_fields = ('image_caption', 'additional_text')
	readonly_fields=('date_updated',)

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()	
	
admin.site.register(Project_Image, Project_Image_Admin)

class Project_Post_Admin(admin.ModelAdmin):
	list_display = ('title', 'category', 'slug',
					'published', 'date_updated')
	search_fields = ('title', 'body')
	readonly_fields=()

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()	
	
admin.site.register(Project_Post, Project_Post_Admin)


class Image_Type_Admin(admin.ModelAdmin):
	list_display = ('image_type_name',)
	search_fields = ('image_type_name',)
	readonly_fields=()

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()	

admin.site.register(Image_Type, Image_Type_Admin)
