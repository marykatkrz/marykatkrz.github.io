from django.views.generic import ListView, DetailView, FormView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.contrib.auth.models import User
from django.core import serializers

from runaway.models import Post, UserProfile
from profiles.forms import UserProfileForm


class CreateLogInView(generic.CreateView):
    form_class=UserCreationForm
    success_url=reverse_lazy('login')
    template_name='signup.html'

class UsernameProfileView(generic.DetailView):
    model=User
    template_name='user_profiles.html'  
    context_object_name='user_profile'
    
    def get_object(self):
        return get_object_or_404(User, username=self.kwargs.get('username'))

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['point_list']=serializers.serialize('json', self.object.post_set.all())
        return context
       
class ProfileView(FormView):
    template_name='user_profiles.html'
    form_class=UserProfileForm

    
    def form_valid(self, form):
        form.save(self.request.user)
        return super(ProfileView, self).form_valid(form)

    def get_success_url(self, *args, **kwargs):
        return reverse('runaway:home')
    
 
class EditUserProfileView(UpdateView): 
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'edit_profile.html'

    def get_object(self):
        user= get_object_or_404(User, username=self.kwargs.get('username'))
        return user.userprofile

    def get_success_url(self, *args, **kwargs):
        return reverse('runaway:home')
