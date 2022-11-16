from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class CreateUserForm(UserCreationForm):
    home_address = forms.CharField(max_length=100)
    phone_number = forms.CharField(max_length=20)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'home_address', 'phone_number']
		
class CustomUserProfile(ModelForm):
    class Meta:

        model = Profile
        fields = '__all__'

        widgets = {
            'user': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'home_address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Home Address'}),
            'latitude': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Latitude'}),
            'longitude': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Longitude'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
        }
#class CustomUserCreationForm(UserCreationForm):
    

#    class Meta:
#        model = User
#        fields = ['username', 'email', 'password', 'password2', 'home_address', 'phone_number']
    
    #def __init__(self, *args, **kwargs):
    #    super(CustomUserCreationForm, self).__init__(*args, **kwargs)

    #    for name, field in self.fields.items():
    #        field.widget.attrs.update({'class': 'input'})



