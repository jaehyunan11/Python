from django.shortcuts import render, HttpResponse

# Create your views here.
def first_view(request):
    return HttpResponse("This method is the first view in app_one")

def second_view(request):
    return HttpResponse("This method is the second view in app_one")