from django.urls import path
from . import views

app_name = "instausers"

urlpatterns = [
    path('', views.index, name='index'),
    path('<pk>/', views.ProfileDetail.as_view(), name='profile-detail'),
]