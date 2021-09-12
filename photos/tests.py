from django.test import TestCase
from django.db import models
from .models import Profile, Image, Location
from django.contrib.auth.models import User

# Create your tests here.
class LocationTestCase(TestCase):    
    def setUp(self):
        self.location = Location(location = 'kisii')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.location, Location))
        
    def test_save_locations(self):
        self.location.save_location()
        all_locations = Location.objects.all()
        self.assertTrue(len(all_locations) > 0)
        
    def test_get_locations(self):
        self.location.save_location()
        all_locations = Location.objects.all()
        self.assertTrue(len(all_locations) > 0)
        
        
class ImageTestCase(TestCase):    
    def setUp(self):
        # Creating a new location and saving it
        self.new_location = Location(location = 'kisii')
        self.new_location.save()
        
        
        # Creating a new Image and saving it
        self.image= Image(image_name = 'falcon', description ='new design', image_file ='images/falcon.jpg', location = self.new_location)
        self.image.save_image()

    def test_save_images(self):
        self.image.save_image()
        all_images = Image.objects.all()
        self.assertTrue(len(all_images) > 0)