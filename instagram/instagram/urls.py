"""instagram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from instausers import views as instausers_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', instausers_views.register, name='register'),
    path('login/', instausers_views.login_user, name='login'),
    path('logout/', instausers_views.logout_user, name='logout'),
    path('', instausers_views.index, name='index'),
    path('user-details/', instausers_views.user_details, name='user-details'),
    path('edit/', instausers_views.profile_edit, name='profile-edit'),
    path('passwordchange/', instausers_views.profile_edit, name='profile-change'),
    path('passwordchange/done/', instausers_views.profile_edit, name='profile-reset'),
    path('profile/', instausers_views.ProfileList.as_view(), name='profile'),
    path('', include('instausers.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
