from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('form/', views.form, name='form'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('success/', views.success, name='success'),
    path('logout/', views.logout, name='test'),
    path('exercise2/', views.exercise2, name='e2'),
    path('exercise2FirstPage/', views.exercise2FirstPage, name='firstpage'),
    path('exercise2SecondPage/', views.exercise2SecondPage, name='secondpage'),
    path('exerice2logout/', views.exercise2logout, name='exercise2logout'),
]