from django.urls import path, include
from .views import PostCreateView
from . import views

app_name = 'instaposts'

urlpatterns = [
   path('', views.likes,  name='post-list'),
   path('like/post/', views.like_post,  name='liked-post'),
   path('post/new/', PostCreateView.as_view(), name="post-create"),
]