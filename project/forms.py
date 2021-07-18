from django import forms
from django.contrib.auth.models import User
from django.forms import fields
from .models import   Project, Profile , Review
from django import forms

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username' , 'first_name' , 'last_name' , 'email')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_photo' , 'bio' ,'profile_photo')

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields =('title' , 'link' ,'image_photo' , 'description')

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('body' , 'post' ,'name')