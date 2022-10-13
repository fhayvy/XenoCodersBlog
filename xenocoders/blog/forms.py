from django.forms import ModelForm
from .models import Post, Category, UserProfile
from django import forms


class  EditProfileForm(forms.ModelForm):
	
	class Meta:
		model = UserProfile
		exclude = ["user"]

        

class PostForm(forms.ModelForm):  
	category = forms.ModelMultipleChoiceField(
		widget=forms.CheckboxSelectMultiple,
		queryset=Category.objects.all(),
		required=True)

	class Meta: 
			model = Post 
			exclude = ['author', 'likes']


class ContactForm(forms.Form):
	first_name = forms.CharField(label="", max_length = 50, widget=forms.TextInput(attrs={'placeholder': 'Your Name'}))
	email_address = forms.EmailField(label="", max_length = 150, widget=forms.TextInput(attrs={'placeholder': 'Your Email address'}))
	message = forms.CharField(label="", widget = forms.Textarea(attrs={'placeholder': 'Your Message'}), max_length = 2000,)