from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")

def create(request):
    return redirect('/')

def show(request, number):
    return HttpResponse(f"placeholder to display blog number {number}.")

def edit(request, number):
    return HttpResponse(f"placeholder to edit blog {number}.")

def destroy(request, number):
    return redirect('/')