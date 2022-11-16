from django.db import models
from django.contrib.auth.models import User
import requests
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    home_address = models.CharField(max_length=200, null=True, blank=True)
    latitude = models.CharField(max_length=50, null=True, blank=True)
    longitude = models.CharField(max_length=50, null=True, blank=True)
    phone_number = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = 'Profile'

    def save(self, *args, **kwargs):
        API_Key = 'AIzaSyDowEwUj5k1z8kPTOolZZwqsmXAgR2T-Dg'
        self.home_address = home_address
        params = {
            'key': API_Key,
            'address': self.home_address
        }

        base_url = 'https://maps.googleapis.com/maps/api/geocode/json?'
        response = requests.get(base_url, params=params).json()
        response.keys()

        if response['status'] == 'OK':
            geometry = response['results'][0]['geometry']
            self.latitude = geometry['location']['lat']
            self.longitude = geometry['location']['lng']
            return super().save(*args, **kwargs)


        #self.latitude =
        #self.longitude =
        #return super().save(*args, **kwargs)

    
    def __str__(self):
        return self.user.username

