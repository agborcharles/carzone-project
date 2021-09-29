from django.db import models

# Create your models here.

class Team(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    twitter_link = models.URLField(max_length=300)
    facebook_link = models.URLField(max_length=300)
    google_link = models.URLField(max_length=300)
    created_date = models.DateTimeField(auto_now_add=True)
