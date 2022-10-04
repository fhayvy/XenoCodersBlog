from django.forms import ModelForm
from .models import Post
from django import forms



class Author(ModelForm):
    class Meta:
        model = Post
        fields = "__all__"


class ContactForm(forms.Form):
	first_name = forms.CharField(max_length = 50)
	last_name = forms.CharField(max_length = 50)
	email_address = forms.EmailField(max_length = 150)
	message = forms.CharField(widget = forms.Textarea, max_length = 2000)