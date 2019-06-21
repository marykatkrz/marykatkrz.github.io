from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name='profiles'

urlpatterns=[
    path('profiles/signup/', views.CreateLogInView.as_view(), name='sign_up'),
    path('<str:username>/edit/', views.EditUserProfileView.as_view(), name='edit_profile'),
    path('profiles/<str:username>/', views.UsernameProfileView.as_view(), name='post_list'),
]   + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)