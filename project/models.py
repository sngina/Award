from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import render , redirect
from django.dispatch import receiver
from django.db.models.signals import post_save
 
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User ,on_delete= models.CASCADE , null=True)
    profile_photo = models.CharField(max_length=30)
    bio = models.CharField(max_length=30)
    image_photo = models.ImageField(upload_to = 'image/' , null = True)
    
    
    def __str__(self):
        return self.user

    def save_profile(self):
        self.save()

    @classmethod
    def delete_image(cls ,id):
        cls.objects.filter(id=id).delete()
    

class Project(models.Model):
    image_photo = models.ImageField(upload_to = 'image/' , null = True)
    title = models.CharField(max_length=60)
    description = models.TextField()
    link = models.CharField(max_length=40)

    def __str__(self):
        return self.title
        #save function
    def save_project(self):
        self.save()
        #delete function

    def delete(self):
        self.delete()

    class Meta:
        ordering = ['image_photo']



class  Review(models.Model):
    post = models.ForeignKey(Project , on_delete= models.CASCADE , related_name= 'review')
    body = models.TextField()
    name =  models.ForeignKey(User , on_delete=models.CASCADE , related_name= 'userprofile')

    def __str__(self):
        return 'Review {} by {}'.format(self.body , self.name)