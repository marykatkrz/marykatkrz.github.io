from django.urls import path

from . import views

app_name='runaway'

urlpatterns=[
    path('', views.PostListView.as_view(), name="home"),
<<<<<<< HEAD
    path('profiles/post/<int:pk>/', views.PostDetailView.as_view(), name='detail'),
    path('profiles/post/create/', views.PostCreateView.as_view(), name='create'),
    path('post/<int:pk>/update', views.PostUpdateView.as_view(), name='update'),
    path('post/<int:pk>/delete', views.PostDeleteView.as_view(), name='delete'),
=======
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='detail'),
    path('register/', views.CreateLogInView.as_view(), name='register'),
    path('post/new/', views.PostCreateView.as_view(), name='create'),
    path('post/<int:pk>/update', views.PostUpdateView.as_view(), name='update'),
    path('post/<int:pk>/delete', views.PostDeleteView.as_view(), name='delete'),
    path('<str:username>/', views.PostList.as_view(), name='post_list'),
>>>>>>> a234bd7e1f4c6e8b44d5edfa225b37e924ed0d06
] 