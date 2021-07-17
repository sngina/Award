from django.db import models

# Create your models here.

# class Profile(models.Model):
#     user = models.OneToOneField(User ,on_delete= models.CASCADE , null=True)
#     profile_photo = models.CharField(max_length=30)
#     bio = models.CharField(max_length=30)
    
#     # search for a profile

class Project(models.Model):
    image_photo = models.ImageField(upload_to = 'image/' , null = True)
    title = models.CharField(max_length=60)
    description = models.TextField()
    link = models.CharField(max_length=40)

    