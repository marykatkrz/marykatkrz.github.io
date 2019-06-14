from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import timedelta
from django.db.models.signals import post_save
from django.dispatch import receiver

class Post(models.Model):
    post=models.TextField(max_length=1000, blank=True)
    username=models.ForeignKey('auth.User', on_delete=models.CASCADE)
    posted=models.DateTimeField(auto_now_add=True)
    edited=models.DateTimeField(auto_now=True)
    location=models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.post

    def get_absolute_url(self):
        return reverse('posts:detail', args=[str(self.id)])

    @property
    def time_diff(self):
        return (self.edited - self.posted)>timedelta(seconds=1)

class UserProfile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    bio=models.TextField(max_length=150, blank=True)
    residence=models.CharField(max_length=50, blank=True)
    
    def __str__(self):
        return self.user.username
    
def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile=UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)
  

  

