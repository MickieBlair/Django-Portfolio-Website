from django.shortcuts import render, redirect
from myadmin.models import Image
from myadmin.models import Page
from myadmin.models import Profile
from myadmin.models import Hobby
from myadmin.models import Accomplishment
from myadmin.models import Education
from myadmin.models import Resume_File
from myadmin.models import Entry
from myadmin.models import External_Link
from projects.models import Project_Image
from projects.models import Slideshow_Project
from projects.models import Current_Project
from projects.models import Project_Category
from projects.models import Project_Language
from projects.models import Project_Feature

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect, FileResponse
from personal.forms import ContactForm
from django.http import FileResponse





def home_screen_view(request, *args, **kwargs):
	context = {}
	context['page_title'] = "Mickie Blair"

	display_categories = Project_Category.objects.filter(display=True).order_by('name')
	context['display_categories'] = display_categories

	display_languages = Project_Language.objects.filter(display=True).order_by('language')
	context['display_languages'] = display_languages

	display_features = Project_Feature.objects.filter(display=True).order_by('feature')
	context['display_features'] = display_features

	if request.GET:
		query = request.GET.get('q', '')
		if query !='':
			return redirect('projects:results_view', query )

	page= Page.objects.filter(page_name="Home", active=True).first()

	git_hub_link = External_Link.objects.filter(link_title="GitHub", active=True).first()
	photo_link = External_Link.objects.filter(link_title="Photography", active=True).first()
	context['git_hub_link'] = git_hub_link
	context['photo_link'] = photo_link


	page_intro = Entry.objects.filter(entry_location="Page Intro", entry_page=page.id, active=True).first()
	context['page_intro'] = page_intro

	current = Entry.objects.filter(entry_location="Current", entry_page=page.id, active=True).first()
	context['current'] = current

	about = Entry.objects.filter(entry_location="About", entry_page=page.id, active=True).first()
	context['about'] = about

	resume = Entry.objects.filter(entry_location="Resume", entry_page=page.id, active=True).first()
	context['resume'] = resume

	contact = Entry.objects.filter(entry_location="Contact", entry_page=page.id, active=True).first()
	context['contact'] = contact

	current_projects = Current_Project.objects.filter(active=True).order_by('order')

	project_slides = Slideshow_Project.objects.filter(active=True).order_by('order')

	context['project_slides'] = project_slides
	context['current_projects'] = current_projects

	return render(request, "personal/home.html", context)

def resume_view(request, *args, **kwargs):
	resume = Resume_File.objects.filter(active=True, file_type="PDF").first()
	response = HttpResponse(resume.res_file, content_type='application/pdf')
	return response

def photo_view(request, slug):
	image = Image.objects.filter(slug=slug).first()

	if image == None:
		image = Project_Image.objects.filter(slug=slug).first()

	response = HttpResponse(image.image, content_type='image/jpeg')
	return response


def about_view(request, *args, **kwargs):
	context = {}
	context['page_title'] = "About Me"
	page = Page.objects.filter(page_name="About", active=True).first()

	images =Image.objects.filter(image_location=page.id, active=True).order_by('order').exclude(order=1)
	image_default = Image.objects.filter(image_location=page.id, order=1, active=True).first()

	profile = Profile.objects.filter(active=True).first()
	hobbies = Hobby.objects.filter(active=True).order_by('order')
	education = Education.objects.filter(active=True).order_by('order')
	accomplishments = Accomplishment.objects.filter(active=True).order_by('order')

	context['images'] = images
	context['image_default'] = image_default
	context['profile'] = profile
	context['hobbies'] = hobbies
	context['education'] = education
	context['accomplishments'] = accomplishments

	return render(request, 'personal/about.html', context)




def contact_success(request, *args, **kwargs):
	context = {}
	context['page_title'] = "Contact"	
	return render(request, 'personal/contact_success.html', context)

def contact_view(request, *args, **kwargs):
	context = {}
	context['page_title'] = "Contact"
	page = Page.objects.filter(page_name="Contact", active=True).first()

	contact_intro = Entry.objects.filter(entry_location="Intro", entry_page=page.id, active=True).first()
	context['contact_intro'] = contact_intro

	contact_sidebar = Entry.objects.filter(entry_location="Sidebar", entry_page=page.id, active=True).order_by('order')
	context['contact_sidebar'] = contact_sidebar

	images =Image.objects.filter(image_location=page.id, active=True).order_by('order').exclude(order=1)
	image_default = Image.objects.filter(image_location=page.id, order=1, active=True).first()
	
	context['images'] = images
	context['image_default'] = image_default

	if request.method == 'GET':
		form = ContactForm()
	else:
		form = ContactForm(request.POST or None)

		if form.is_valid():
			name = form.cleaned_data['name']
			subject = form.cleaned_data['subject']
			email = form.cleaned_data['from_email']
			message = form.cleaned_data['message']
			new_subject = "Contact Form: " + name + " - " + subject
			new_message = "Email: " + email + "\n\n" + "Message: " + message

			from_email = 'contact@mickieblair.com'

			try:
				send_mail(new_subject, new_message, from_email, ['contact@mickieblair.com'])
			except BadHeaderError:
				print("except")
				return HttpResponse('Invalid header found.')

			return redirect('contact_success')

	context['form'] = form

	return render(request, 'personal/contact.html', context)


