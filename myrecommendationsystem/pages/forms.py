from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class UserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2','first_name','last_name']


# class ContactUsForm(forms.ModelForm):
# 	class Meta:
# 		model = Contactus
# 		fields = [
# 			'name',
# 			'emails',
# 			'subjects',
# 			'descriptions'
# 	]


