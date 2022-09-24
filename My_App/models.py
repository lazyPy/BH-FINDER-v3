from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    username = models.CharField(unique=True, max_length=200, null=True)
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    phone = models.IntegerField(verbose_name='Contact Number')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.name


class BoardingHouse(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    phone = models.IntegerField(verbose_name='Contact Number')
    location = models.CharField(max_length=200)
    latitude = models.FloatField(verbose_name="Latitude", max_length=50, null=True, blank=True)
    longitude = models.FloatField(verbose_name="Longitude", max_length=50, null=True, blank=True)
    detail = models.CharField(max_length=200)
    picture = models.ImageField(upload_to='bh-images/')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name
