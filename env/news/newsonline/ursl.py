from django.shortcuts import render

urlpatterns = [
    path('', views.home, name='home'),
]