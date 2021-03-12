from django.db import models
import re
from datetime import datetime

# Create your models here.

class UserManager(models.Manager):
    def validator(self, postdata):
        email_check=re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        errors={}
        if len(postdata['name'])<2:
            errors['name']="Name must be longer than 2 characters"
        if len(postdata['alias'])<1:
            errors['alias']="Must have an alias name"
        if not email_check.match(postdata['email']): 
            errors['email']="Email must be valid format!"
        if len(postdata['pw'])<8:
            errors['pw']="Password must be at least 8 characters!"
        if postdata['pw'] != postdata['conf_pw']:
            errors['conf_pw']="Password and confirm password must match!"
        return errors

class User(models.Model):
    name=models.CharField(max_length=255)
    alias=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    birth= models.DateTimeField()
    friends=models.ManyToManyField("self", related_name="my_friends")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=UserManager()

#class Friend(models.Model):
    #users = models.ManyToManyField(User, related_name='friend')
    #current_user = models.ForeignKey(User, related_name='owner', null=True, on_delete = models.CASCADE)