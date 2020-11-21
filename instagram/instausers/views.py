from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from .forms import RegisterUserForm

# Create your views here.

def index(request):
    return render(request, 'instausers/index.html')

def register(request, *arg, **kwargs):
    user = request.user
    if user.is_authenticated:
        return HttpResponse('You are already authenticated as {user.email}.')
    context = {}

    if request.POST:
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            email.cleaned_data.get('email').lower()
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            destination = kwargs.get('next')
            if destination:
                return redirect(destination)
            return redirect('register')
        else:
            context['register_form'] = form

    return render(request, 'instausers/register.html', context)



 

