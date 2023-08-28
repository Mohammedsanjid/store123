from django.db import models

# Create your models here.

class UserModel(models.Model):
    username = models.CharField(max_length=255,null=True,blank=True)
    password = models.CharField(max_length=255,null=True,blank=True)