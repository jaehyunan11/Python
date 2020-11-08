# Create a new Django Project
 - django-admin startproject (your_project_name_here)
  ex) django-admin startproject first_project

# Running server
 - python manage.py runserver

# Create a new App in our Django Project

 - python manage.py startapp (your_project_name_here)
  ex) python manage.py startapp new_app

# After adding new app in Django Project
 1) Add installed_app in following location 
  - your_project_name_here/your_project_name_here/settings.py

 2) Update path in urls.py
  - your_project_name_here/your_project_name_here/urls.py
  from django.urls import path, include  # import include
# from django.contrib import admin  # comment out, or just delete
  urlpatterns = [
    path('', include('your_app_name_here.urls')),	   
    # path('admin/', admin.sites.urls) # comment out, or just delete
]

 3) create a new urls.py in the your_app_name_here folder
  - your_project_name_here/your_app_name_here/urls.py
  from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),	   
]

 4) Put a function called index in our app's view.py file
  - your_project_name_here/your_app_name_here/views.py
  from django.shortcuts import render, HttpResponse
def index(request):
    return HttpResponse("This is my response!")