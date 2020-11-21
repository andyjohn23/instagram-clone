from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('user-details/', views.user_details, name='user-details')
]