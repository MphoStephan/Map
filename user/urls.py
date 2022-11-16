from django.urls import path
from . import views


urlpatterns = [
    path('', views.loginPage, name='login'), 
    path('login/', views.loginPage, name='login'), 
    path('register/', views.registerPage, name='registerPage'),
    path('map/', views.userLocation, name='map'),
    path('profile/', views.createProfile, name='profile'),

    path('logout/', views.logoutUser, name='logout'),
]