from django.contrib import admin
from myadmin.models import Image
from myadmin.models import Page
from myadmin.models import Profile
from myadmin.models import Hobby
from myadmin.models import Accomplishment
from myadmin.models import Education
from myadmin.models import Resume_File
from myadmin.models import Entry
from myadmin.models import External_Link

#Register your models here.
class External_Link_Admin(admin.ModelAdmin):
	list_display = ('link_title', "link_url",'active', 'date_created', 'date_updated')
	search_fields = ()
	readonly_fields=('date_created', 'date_updated')

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()	
	
admin.site.register(External_Link, External_Link_Admin)

class Entry_Admin(admin.ModelAdmin):
	list_display = ('entry_page', "entry_location",'title', 'active', 'date_created', 'date_updated')
	search_fields = ()
	readonly_fields=('date_created', 'date_updated')

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()	
	
admin.site.register(Entry, Entry_Admin)

class Resume_File_Admin(admin.ModelAdmin):
	list_display = ('title', 'file_type','active', 'date_created', 'date_updated')
	search_fields = ()
	readonly_fields=('date_created', 'date_updated')

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()	
	
admin.site.register(Resume_File, Resume_File_Admin)


class Education_Admin(admin.ModelAdmin):
	list_display = ('type_edu', 'order', 'desc', 'active', 'school', 'year', 'location', 'date_created', 'date_updated')
	search_fields = ()
	readonly_fields=('date_created', 'date_updated')

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()	
	
admin.site.register(Education, Education_Admin)

class Hobby_Admin(admin.ModelAdmin):
	list_display = ('hobby_name', 'active',  'order','date_created', 'date_updated')
	search_fields = ()
	readonly_fields=('date_created', 'date_updated')

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()	
	
admin.site.register(Hobby, Hobby_Admin)

class Accomplishment_Admin(admin.ModelAdmin):
	list_display = ('acc_name', 'active',  'order','date_created', 'date_updated')
	search_fields = ()
	readonly_fields=('date_created', 'date_updated')

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()	
	
admin.site.register(Accomplishment, Accomplishment_Admin)


class Image_Admin(admin.ModelAdmin):
	list_display = ('image_caption', 'image', 'image_location', 'order', 'active', 'date_created', 'date_updated')
	search_fields = ()
	readonly_fields=('date_created', 'date_updated')

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()	
	
admin.site.register(Image, Image_Admin)


class Page_Admin(admin.ModelAdmin):
	list_display = ('page_name', 'link_url', 'active', 'date_created', 'date_updated')
	search_fields = ()
	readonly_fields=('date_created', 'date_updated')

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()	
	
admin.site.register(Page, Page_Admin)

class Profile_Admin(admin.ModelAdmin):
	list_display = ('title', 'profile_location', 'active', 'date_created', 'date_updated')
	search_fields = ()
	readonly_fields=('date_created', 'date_updated')

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()	
	
admin.site.register(Profile, Profile_Admin)