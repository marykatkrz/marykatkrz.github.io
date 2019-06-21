from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView 
from django.urls import reverse_lazy
from django.shortcuts import render
from django. contrib.auth.forms import UserCreationForm
<<<<<<< HEAD
from django.contrib.auth.decorators import login_required
=======
from django.views import generic
>>>>>>> a234bd7e1f4c6e8b44d5edfa225b37e924ed0d06

from .models import Post, UserProfile


class PostListView(ListView):
    model = Post
    template_name = 'home.html'

    def get_queryset(self):
        return Post.objects.all().order_by('-posted')

class PostDetailView(DetailView):
    model=Post
<<<<<<< HEAD
    template_name='popup_view.html' 
=======
    template_name='user_profiles.html'
    
class PostCreateView(CreateView):
    model=Post
    template_name='get_create.html'
    fields=['username','location', 'post']
    success_url=reverse_lazy('runaway:home')

    def if_valid(self, form):
        form.instance.username=self.request.username
        return super().if_valid
>>>>>>> a234bd7e1f4c6e8b44d5edfa225b37e924ed0d06

class PostUpdateView(UpdateView):
    model=Post
    template_name='get_update.html'
<<<<<<< HEAD
    fields=['description','post']
=======
    fields=['post']
>>>>>>> a234bd7e1f4c6e8b44d5edfa225b37e924ed0d06
    success_url=reverse_lazy('runaway:home')
 

class PostDeleteView(DeleteView):
    model=Post
    template_name='get_delete.html'
    success_url=reverse_lazy('runaway:home')

<<<<<<< HEAD

class PostCreateView(CreateView):
    model=Post
    template_name='get_create.html'
    fields=['location', 'lng', 'lat', 'description', 'post']
    success_url=reverse_lazy('runaway:home')
    
    def form_valid(self, form):
        form.instance.username=self.request.user
        form.save()
        return super().form_valid(form)

=======
class CreateLogInView(generic.CreateView):
    form_class=UserCreationForm
    success_url=reverse_lazy('login')
    template_name='register.html'

class UsernameListView(generic.DetailView):
    model=UserProfile
    template_name='user_profiles.html'

class PostList(generic.ListView):
    model=Post
    template_name='user_profiles.html'  
>>>>>>> a234bd7e1f4c6e8b44d5edfa225b37e924ed0d06
