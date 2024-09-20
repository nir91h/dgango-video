from django.urls import path
from . import views

urlpattern =[
    path('login/', views.login),
    path('register/', views.register)
]