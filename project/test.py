from django.test import TestCase
from .models import Profile , Review , Project

class ProfileTestClass(TestCase):
    def setUp(self):
        self.profile = Profile(bio='image')
    def test_instance(self):
        self.assertTrue(isinstance(self.profile , Profile))
    def test_save_method(self):
        self.profile.save()
        bio_pic = Profile.objects.all()
        self.assertTrue(len(bio_pic) >0)

class   ReviewTestClass(TestCase):
    def setUp(self):
        self.review = Review(bio = 'review')
    
    def test_instance(self):
        self.assertTrue(isinstance(self.review , Review))
