from django import forms

from projects.models import Project_Language
from projects.models import Project_Status
from projects.models import Project_Category
from projects.models import Project_Album
from projects.models import Project_Image
from projects.models import Project_Post
# from projects.models import Post


# class Post_Form(forms.ModelForm):
# 	class Meta:
# 		model = Post
# 		fields=['title', 'body', 'published', 'github']

		
class Project_Language_Form(forms.ModelForm):
	class Meta:
		model = Project_Language
		fields = ['language',]

class Project_Status_Form(forms.ModelForm):
	class Meta:
		model = Project_Status
		fields = ['status',]

class Project_Category_Form(forms.ModelForm):
	class Meta:
		model = Project_Category
		fields = ['name',]


class Create_Image_Form(forms.ModelForm):
	class Meta:
		model = Project_Image
		fields = ['order', 'image', 'published_image',
			'image_caption',  'default_image', 'additional_text']#'album', 'image_type', 'slug'

class Edit_Image_Form(forms.ModelForm):
	class Meta:
		model = Project_Image
		fields = ['order', 'image', 'published_image',
			'image_caption',  'default_image', 'additional_text']#'album', 'image_type', 'slug'

	def save(self, commit=True):
		image = self.instance
		image.order = self.cleaned_data['order']
		image.published_image = self.cleaned_data['published_image']
		image.default_image = self.cleaned_data['default_image']
		image.image_caption = self.cleaned_data['image_caption']
		image.additional_text = self.cleaned_data['additional_text']		

		if self.cleaned_data['image']:
			image.image = self.cleaned_data['image']		

		if commit:
			image.save()
		return image



class Create_Project_Album_Form(forms.ModelForm):
	class Meta:
		model = Project_Album
		fields = ['album_name', 'album_description','published_album'] #'project_name', 

	def clean_album_name(self):
		album_name = self.cleaned_data['album_name']
		try:
			album = Project_Album.objects.exclude(pk=self.instance.pk).get(album_name=album_name)
		except Project_Album.DoesNotExist:
			return album_name
		raise forms.ValidationError('Album name "%s" is already in use.' % album)


class Update_Project_Album_Form(forms.ModelForm):
	class Meta:
		model = Project_Album
		fields = ['album_name', 'album_description','published_album']
		exclude = ('project_name',)

	def clean_album_name(self):
		print("cleaning Album name")
		album_name = self.cleaned_data['album_name']
		try:
			project_album = Project_Album.objects.exclude(pk=self.instance.pk).get(album_name=album_name)
		except Project_Album.DoesNotExist:
			return album_name
		raise forms.ValidationError('Album Name "%s" is already in use.' % project_album)

	def save(self, commit=True):
		project_album = self.instance
		project_album.album_name = self.cleaned_data['album_name']
		project_album.album_description = self.cleaned_data['album_description']
		project_album.published_album = self.cleaned_data['published_album']

		if commit:
			project_album.save()
		return project_album


class Create_Project_Post_Form(forms.ModelForm):
	
	class Meta:
		model = Project_Post
		fields = ['title', 'body', 'published', 'github']

	def clean_title(self):
		title = self.cleaned_data['title']
		try:
			project_post = Project_Post.objects.exclude(pk=self.instance.pk).get(title=title)
		except Project_Post.DoesNotExist:
			return title
		raise forms.ValidationError('Title "%s" is already in use.' % project_post)



class Update_Project_Post_Form(forms.ModelForm):
	class Meta:
		model = Project_Post
		fields = ['title', 'body', 'published', 'github']
		exclude = ('category', 'languages', 'status', 'album')

	def clean_title(self):
		title = self.cleaned_data['title']
		try:
			project_post = Project_Post.objects.exclude(pk=self.instance.pk).get(title=title)
		except Project_Post.DoesNotExist:
			return title
		raise forms.ValidationError('Title "%s" is already in use.' % project_post)

	def save(self, commit=True):
		project_post = self.instance
		project_post.title = self.cleaned_data['title']
		project_post.body = self.cleaned_data['body']
		project_post.published = self.cleaned_data['published']
		project_post.github = self.cleaned_data['github']

		if commit:
			project_post.save()
		return project_post