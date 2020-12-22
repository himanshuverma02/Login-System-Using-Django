from django.urls import path

from . import views

urlpatterns =[
path('',views.home,name='home'),
path('loginpage', views.loginpage , name='loginpage'),
path('signup', views.signup, name='signup'),
path('userlogin',views.userlogin, name='userlogin'),
path('form',views.form, name= 'form')
]