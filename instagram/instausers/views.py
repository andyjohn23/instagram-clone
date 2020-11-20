from django.shortcuts import render,redirect
from .forms import RegisterUserForm

# Create your views here.

def index(request):
    return render(request, 'instausers/index.html')

def register(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    else:
        form = RegisterUserForm()
    return render(request, 'instausers/register.html', {'form': form, 'title': 'register'})



 

