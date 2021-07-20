from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Profile, Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('user' , 'image_photo' ,'title' ,'description','link')

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user' , 'profile_photo' , 'bio' ,'image_photo')

