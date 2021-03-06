from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import Profile, Project, Rating


class RegisterUserForm(UserCreationForm):
    class Meta:
        model= User
        fields= ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


class LoginUserForm(forms.Form):

    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}), max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget.attrs['class'] = 'form-control'


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'bio']

        widgets = {
            'avatar': forms.FileInput(attrs={'class': 'form-control my-1'}),
            'bio': forms.Textarea(attrs={'class': 'form-control my-1'})
        }

class UploadProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'projectImage', 'description', 'projectUrl']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'projectImage': forms.FileInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control my-1'}),
            'projectUrl': forms.TextInput(attrs={'class': 'form-control'})
        }

class ReviewProjectForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['design', 'usability', 'content']

        widgets = {
            'design': forms.NumberInput(attrs={'class': 'form-control'}),
            'usability': forms.NumberInput(attrs={'class': 'form-control'}),
            'content': forms.NumberInput(attrs={'class': 'form-control'})
        }