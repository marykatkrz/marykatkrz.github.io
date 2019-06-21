from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView 
from django.urls import reverse_lazy
from django.shortcuts import render
from django. contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from .models import Post, UserProfile


class PostListView(ListView):
    model = Post
    template_name = 'home.html'

    def get_queryset(self):
        return Post.objects.all().order_by('-posted')

class PostDetailView(DetailView):
    model=Post
    template_name='popup_view.html' 

class PostUpdateView(UpdateView):
    model=Post
    template_name='get_update.html'
    fields=['description','post']
    success_url=reverse_lazy('runaway:home')
 

class PostDeleteView(DeleteView):
    model=Post
    template_name='get_delete.html'
    success_url=reverse_lazy('runaway:home')


class PostCreateView(CreateView):
    model=Post
    template_name='get_create.html'
    fields=['location', 'lng', 'lat', 'description', 'post']
    success_url=reverse_lazy('runaway:home')
    
    def form_valid(self, form):
        form.instance.username=self.request.user
        form.save()
        return super().form_valid(form)

