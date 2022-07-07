from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

# Create your models here.

#class to crete a Usermodel Manager for Blog API
class BlogUserManager(BaseUserManager):

    #To create a new user
    def create_user(self,userid,email,name,password):

        if not userid and not email:
            raise ValueError('Every User must contain a userid and email')
        
        email=self.normalize_email(email=email)
        blog_user=self.model(userid=userid,email=email,name=name)
        blog_user.set_password(password)
        blog_user.save(using=self._db)

        return blog_user

    #To create a superuser
    def create_superuser(self,userid,email,name,password):

        blog_user=self.create_user(userid=userid,email=email,name=name,password=password)
        blog_user.is_superuser=True
        blog_user.is_staff=True
        blog_user.save(using=self._db)

        return blog_user


#class to create a Usermodel of Blog API
class BlogUserModel(AbstractBaseUser,PermissionsMixin):
    
    #Fields that are required for an user
    userid=models.CharField(max_length=25,unique=True)
    email=models.EmailField(max_length=255,unique=True)
    name=models.CharField(max_length=255)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)

    #Main Fields
    USERNAME_FIELD='userid'
    REQUIRED_FIELDS=['email','name']

    objects=BlogUserManager()

    def get_name(self):
        return self.name

    def get_userid(self):
        return self.userid

    def __str__(self):
        return self.userid


#Classs for BlogPostModel
class BlogPostModel(models.Model):
    post_profile=models.ForeignKey(
        settings.AUTH_USER_MODEL ,
        on_delete=models.CASCADE
    )

    title=models.CharField(max_length=100)
    post=models.CharField(max_length=500)

    def __str__(self):
        return self.title