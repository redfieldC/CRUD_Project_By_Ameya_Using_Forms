from django.db import models

# Create your models here.
class Members(models.Model):
    firstname = models.CharField(max_length=20,blank=True,null=True)
    lastname = models.CharField(max_length=20,blank=True,null=True)
    age = models.IntegerField(default=0,blank=True,null=True)
    year_of_birth =  models.IntegerField(default=1970,blank=True,null=True)