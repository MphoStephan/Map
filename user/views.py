from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import CreateUserForm, CustomUserProfile
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from .models import Profile
# Create your views here.

def loginPage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('map')
        else:
            messages.info(request, 'Username OR password is incorrect')
    return render(request, 'login.html')



def registerPage(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account successfully created ' + user)
            return redirect('login')

    context = {'form':form }
    return render(request, 'register.html', context)

@login_required(login_url='login')
def userLocation(request):
    return render(request, 'map.html')

def createProfile(request):
    form = CustomUserProfile()

    if request.method == 'POST':
        form = CustomUserProfile(request.POST)
        if form.is_valid():
            form.save()
            return redirect('map')

    context = {
        'form': form
    }
    return render(request, 'profile.html', context)




def logoutUser(request):
    logout(request)
    messages.info(request, 'Username was succesfully logout')
    return redirect('login')