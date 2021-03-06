from django import forms
from captcha.fields import CaptchaField

class ContactForm(forms.Form):
	name = forms.CharField(required=True)
	from_email = forms.EmailField(required=True)
	subject = forms.CharField(required=True)
	message = forms.CharField(widget=forms.Textarea, required=True)
	captcha = CaptchaField()