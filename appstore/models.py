from msilib.schema import Class
from optparse import TitledHelpFormatter
from django.db import models
from django.utils import timezone
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth import get_user_model
from embed_video.fields import EmbedVideoField



# Create your models here.
class Members(models.Model):
    fname=models.CharField(max_length=255)
    lname=models.CharField(max_length=255)

class movies(models.Model):
  title = models.CharField(max_length=255, blank=False)
  released_date= models.DateField()
  main_actor = models.CharField(max_length=255)
  Genre_choice = (
        ('action', 'ACTION'),
        ('comedy', 'COMEDY'),
    )
  genre= models.CharField(max_length=10, choices=Genre_choice)
  description = models.CharField(max_length=255)
  video = models.FileField(upload_to='videos_uploaded',
  validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])
  thumbnail = models.ImageField(upload_to='thumbnail')
  url = models.CharField(max_length=255)
  user_id = models.CharField(max_length=255)



class Customers(models.Model):
    Gender_choice = (
        ('male', 'MALE'),
        ('female', 'FEMALE'),
    )
    firstName = models.CharField(max_length=40)
    lastName = models.CharField(max_length= 70)
    Gender = models.CharField(max_length=20, choices=Gender_choice,default='other') 
    Age = models.IntegerField()
    Profile = models.ImageField()
    RegistrationDate = models.DateField()

class AddMovie(models.Model):
    title = models.CharField(max_length=40)
    releasedDate = models.DateField()
    mainActor = models.CharField(max_length=35)
    Genre_choice = (
        ('action', 'ACTION'),
        ('comedy', 'COMEDY'),
    )
    Genre = models.CharField(max_length=10, choices=Genre_choice)
    moviePoster = models.ImageField(null=True)
    
    def __str__(self): 
        return f"{self.title}{self.releasedDate}{self.mainActor}{self.Genre}{self.moviePoster}{self.url}"

class addMessage(models.Model):
    Username = models.CharField(max_length=50)
    Email = models.EmailField(max_length=100)
    Subject = models.CharField(max_length=100)
    Message = models.CharField(max_length=400)
    def __str__(self): 
        return f"{self.Username}{self.Message}"

class addUpComing(models.Model):
    Title = models.CharField(max_length=100)
    mainActor = models.CharField(max_length=70)
    GenreOptions = (
        ('action', 'ACTION'),
        ('comedy', 'COMEDY')
    )
    dateTobeOut = models.DateField()
    Genre = models.CharField(max_length=50, choices=GenreOptions)

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    Gender_choice = (
        ('male', 'MALE'),
        ('female', 'FEMALE'), 
    )
    FirstName = models.CharField(max_length= 70)
    LastName = models.CharField(max_length= 70)
    bio= models.TextField()
    ProfilePic = models.ImageField(null= True, blank= True, upload_to="images/profiles")
    Gender = models.CharField(max_length=20, choices=Gender_choice,default='other') 
    Age = models.IntegerField()
    Profile = models.ImageField()
    RegistrationDate = models.DateField()
    def __str__(self):
        return str(self.user)

        


class Item(models.Model):
    video = EmbedVideoField()

