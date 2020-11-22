from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from .forms import RegisterUserForm, AuthenticationForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.contrib.auth.views import PasswordChangeView,PasswordResetDoneView
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from .models import Profile,UserAccount

# Create your views here.


def index(request):

    context = {}

    user = request.user
    if user.is_authenticated:
        return redirect('profile')

    destination = get_redirect_if_exists(request)
    if request.POST:
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                destination = get_redirect_if_exists(request)
                if destination:
                    return redirect(destination)
                return redirect('index')

        else:
            context['login_form'] = form

    return render(request, 'instausers/index.html', context)


def register(request, *arg, **kwargs):
    user = request.user

    if user.is_authenticated:
        return HttpResponse('You are already authenticated as { user.email }.')
    context = {}

    if request.POST:
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email').lower()
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            destination = get_redirect_if_exists(request)
            if destination:
                return redirect(destination)
            return redirect('profile')
        else:
            context['register_form'] = form

    return render(request, 'instausers/register.html', context)


def logout_user(request, *args, **kwargs):
    logout(request)
    return redirect("index")


def login_user(request, *args, **kwargs):

    context = {}

    user = request.user
    if user.is_authenticated:
        return redirect('profile')

    destination = get_redirect_if_exists(request)
    if request.POST:
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                destination = get_redirect_if_exists(request)
                if destination:
                    return redirect(destination)
                return redirect('index')

        else:
            context['login_form'] = form

    return render(request, 'instausers/login.html', context)


def get_redirect_if_exists(request):
    redirect = None
    if request.GET:
        if request.GET.get('next'):
            redirect = str(request.GET.get('next'))

    return redirect

@login_required(login_url='login')
def profile_edit(request):

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Profile updated successfully')
            return redirect('profile-edit')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'instausers/profile_edit.html', context)

@login_required(login_url='login')
def user_details(request):

    return render(request, 'instausers/instauser-details.html')

@method_decorator(login_required, name='dispatch')
class ProfileList(ListView):
    model = Profile
    template_name = 'instausers/profile.html'
    context_object_name = 'profiles'

    def get_queryset(self):
        return Profile.objects.all().exclude(user=self.request.user)

@method_decorator(login_required, name='dispatch')
class ProfileDetail(DetailView):
    model = Profile
    template_name = 'instausers/profile-detail.html'
    

    


