from django.shortcuts import render,redirect
from .forms import RegisterUserForm

# Create your views here.

def index(request):
    form = RegisterUserForm()

    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')
            
    context = {'form':form}
    return render(request, 'instausers/index.html', context)

def register(request):
    form = RegisterUserForm()

    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            
    context = {'form':form}
    return render(request, 'instausers/register.html', context)



 

