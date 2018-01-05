from django.forms import ModelForm,TextInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Person, level
from django import forms


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    


class PersonForm(ModelForm) :
	class Meta:
		model = Person
		fields = ['phoneno','college']     



class LevelIncreaseForm(ModelForm):
	class Meta:
		model= level
		exclude = ['levelnumber','pic']		  
		widgets = {
            'ans': TextInput(attrs={'autocomplete': 'off'}),
        }


