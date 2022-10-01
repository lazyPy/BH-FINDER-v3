from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.models import Group

from .decorators import unauthenticated_user, admin_only, user_only


# Create your views here.

@unauthenticated_user
def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('admin-page')
        else:
            print('Username OR password is incorrect')

    return render(request, 'login.html')


@unauthenticated_user
def registerUser(request):
    form = UserForm()

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='user')
            user.groups.add(group)
            return redirect('login')

    context = {
        'form': form,
    }
    return render(request, 'register.html', context)


@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
@admin_only
def adminPage(request):
    boarding_houses = BoardingHouse.objects.all()

    context = {
        'boarding_houses': boarding_houses,
    }
    return render(request, 'admin-page.html', context)


@login_required(login_url='login')
@user_only
def homePage(request):
    boarding_houses = BoardingHouse.objects.all()

    context = {
        'boarding_houses': boarding_houses,
    }
    return render(request, 'home.html', context)


@login_required(login_url='login')
@user_only
def myBh(request, pk):
    boarding_houses = BoardingHouse.objects.all()

    context = {
        'boarding_houses': boarding_houses,
    }
    return render(request, 'my-bh.html', context)


@login_required(login_url='login')
@user_only
def bhDetail(request, pk):
    bh = BoardingHouse.objects.get(id=pk)

    context = {
        'bh': bh,
    }
    return render(request, 'bh-detail.html', context)


@login_required(login_url='login')
@user_only
def addBH(request):
    if request.method == 'POST':
        BoardingHouse.objects.create(
            owner=request.user,
            name=request.POST.get('name'),
            description=request.POST.get('description'),
            phone=request.POST.get('phone'),
            location=request.POST.get('location'),
            latitude=request.POST.get('latitude'),
            longitude=request.POST.get('longitude'),
            picture1=request.FILES.get('picture1'),
            picture2=request.FILES.get('picture2'),
            picture3=request.FILES.get('picture3')
        )

        return redirect('home')
    return render(request, 'add-bh.html')


@login_required(login_url='login')
@user_only
def deleteBH(request, pk):
    bh = BoardingHouse.objects.get(id=pk)
    bh.delete()
    return redirect('my-bh', pk)


@login_required(login_url='login')
@user_only
def editBH(request, pk):
    bh = BoardingHouse.objects.get(id=pk)

    context = {
        'bh': bh,
    }
    return render(request, 'edit-bh.html', context)


@login_required(login_url='login')
@user_only
def updateBH(request, pk):
    bh = BoardingHouse.objects.get(id=pk)
    bh.name = request.POST['name']
    bh.owner = request.user
    bh.description = request.POST['description']
    bh.phone = request.POST['phone']
    bh.location = request.POST['location']
    bh.latitude = request.POST['latitude']
    bh.longitude = request.POST['longitude']
    bh.picture1 = request.FILES['picture1']
    bh.picture2 = request.FILES['picture2']
    bh.picture3 = request.FILES['picture3']
    bh.save()

    return redirect('my-bh', pk)


def adminBHDetail(request, pk):
    bh = BoardingHouse.objects.get(id=pk)

    if bh.admin_approval:
        bh.admin_approval = 'APPROVED'
    else:
        bh.admin_approval = 'DENIED'

    if request.method == 'POST':
        bh.admin_approval = request.POST['admin_approval']
        if bh.admin_approval == 'APPROVED':
            bh.admin_approval = True
            bh.save(update_fields=['admin_approval'])
            bh.admin_approval = 'APPROVED'
        else:
            bh.admin_approval = False
            bh.save(update_fields=['admin_approval'])
            bh.admin_approval = 'DENIED'

    context = {
        'bh': bh,
        'status': bh.admin_approval
    }

    return render(request, 'bh-detail.html', context)
