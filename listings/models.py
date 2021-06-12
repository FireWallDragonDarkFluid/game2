from django.db import models
from datetime import datetime 

# Create your models here.
class Listing(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    tag = models.CharField(max_length=200,blank=True)
    img = models.CharField(max_length=200,blank=True)
    index = models.CharField(max_length=200,blank=True)
    inner_img1 = models.CharField(max_length=200,blank=True)
    inner_img2 = models.CharField(max_length=200,blank=True)
    inner_img3 = models.CharField(max_length=200,blank=True)
    os = models.CharField(max_length=200,blank=True)
    processor = models.CharField(max_length=200,blank=True)
    memory = models.CharField(max_length=200,blank=True)
    graphics = models.CharField(max_length=200,blank=True)
    directX = models.CharField(max_length=200,blank=True)
    storage = models.CharField(max_length=200,blank=True)
    video = models.CharField(max_length=200,blank=True)
    description = models.CharField(max_length=500,blank=True)
    def __str__(self):
        return self.name


