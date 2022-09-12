from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginUser, name='login'),
    path('register/', views.registerUser, name='register'),
    path('logout/', views.logoutUser, name='logout'),

    path('', views.homePage, name='home'),
    path('<str:pk>/my-boarding-house/', views.myBh, name='my-bh'),
    path('<str:pk>/profile/', views.profile, name='profile'),
    path('<str:pk>/boarding-house-detail/', views.bhDetail, name='bh-detail'),
]