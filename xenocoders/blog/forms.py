from django.forms import ModelForm
from .models import Post
from django import forms



class Author(ModelForm):
    class Meta:
        model = Post
        fields = "__all__"


class ContactForm(forms.Form):
	first_name = forms.CharField(label="", max_length = 50, widget=forms.TextInput(attrs={'placeholder': 'Your Name'}))
	email_address = forms.EmailField(label="", max_length = 150, widget=forms.TextInput(attrs={'placeholder': 'Your Email address'}))
	message = forms.CharField(label="", widget = forms.Textarea(attrs={'placeholder': 'Your Message'}), max_length = 2000,)