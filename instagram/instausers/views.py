from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login,logout,authenticate
from .forms import RegisterUserForm, AuthenticationForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
def profile(request):

    return render(request, 'instausers/profile.html')

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
