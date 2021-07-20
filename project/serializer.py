from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('user' , 'image_photo' ,'title' ,'description','link')