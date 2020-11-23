from django.urls import path
from . import views

app_name = "instausers"

urlpatterns = [
    path('<pk>/', views.ProfileDetail.as_view(), name='profile-detail'),
    path('profile/', views.ProfileList.as_view(), name='profile'),
    path('profile/follow/', views.unfollow_follow, name='follow-profile'),
]