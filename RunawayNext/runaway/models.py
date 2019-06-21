from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import timedelta
from django.db.models.signals import post_save
from django.dispatch import receiver

class Post(models.Model):
<<<<<<< HEAD
    post=models.TextField()
    description=models.CharField(max_length=300)
    username=models.ForeignKey('auth.User', on_delete=models.CASCADE)
    posted=models.DateTimeField(auto_now_add=True)
    edited=models.DateTimeField(auto_now=True)
    location=models.CharField(max_length=150)
    lat=models.FloatField()
    lng=models.FloatField()
    
=======
    post=models.TextField(max_length=1000, blank=True)
    username=models.ForeignKey('auth.User', on_delete=models.CASCADE)
    posted=models.DateTimeField(auto_now_add=True)
    edited=models.DateTimeField(auto_now=True)
    location=models.CharField(max_length=50, blank=True)
>>>>>>> a234bd7e1f4c6e8b44d5edfa225b37e924ed0d06

    def __str__(self):
        return self.post

    def get_absolute_url(self):
        return reverse('posts:detail', args=[str(self.id)])

    @property
    def time_diff(self):
        return (self.edited - self.posted)>timedelta(seconds=1)

class UserProfile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
<<<<<<< HEAD
    name=models.CharField(max_length=50, blank=True)
    bio=models.TextField(max_length=150, blank=True)
    residence=models.CharField(max_length=100, blank=True)
    image=models.ImageField(upload_to='user_profiles', blank=True)
=======
    bio=models.TextField(max_length=150, blank=True)
    residence=models.CharField(max_length=50, blank=True)
>>>>>>> a234bd7e1f4c6e8b44d5edfa225b37e924ed0d06
    
    def __str__(self):
        return self.user.username
    
def create_profile(sender, **kwargs):
<<<<<<< HEAD
    user=kwargs["instance"]
    if kwargs['created']:
        user_profile=UserProfile(user=user)
        user_profile.save()

post_save.connect(create_profile, sender=User)

=======
    if kwargs['created']:
        user_profile=UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)
>>>>>>> a234bd7e1f4c6e8b44d5edfa225b37e924ed0d06
  

  

