from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import *


# Create your views here.

def loginUser(request):
    if request.user.is_authenticated:
        return redirect('home')

    form = LoginForm()

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.user_cache)
            return redirect('home')

    context = {
        'form': form
    }

    return render(request, 'login.html', context)


def registerUser(request):
    form = UserForm()

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    context = {
        'form': form,
    }
    return render(request, 'register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


def homePage(request):
    form = BoardingHouseForm()
    boarding_houses = BoardingHouse.objects.all()

    if request.method == 'POST':
        BoardingHouse.objects.create(
            owner=request.user,
            name=request.POST.get('name'),
            description=request.POST.get('description'),
            phone=request.POST.get('phone'),
            location=request.POST.get('location'),
            detail=request.POST.get('detail'),
            picture=request.FILES.get('picture'),
        )
        return redirect('home')

    context = {
        'form': form,
        'boarding_houses': boarding_houses,
    }
    return render(request, 'home.html', context)


def myBh(request, pk):
    boarding_houses = BoardingHouse.objects.all()

    context = {
        'boarding_houses': boarding_houses,
    }
    return render(request, 'my-bh.html', context)


def profile(request, pk):
    return render(request, 'profile.html')


def bhDetail(request, pk):
    bh = BoardingHouse.objects.get(id=pk)

    context = {
        'bh': bh,
    }
    return render(request, 'bh-detail.html', context)
