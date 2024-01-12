from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request,'core/index.html')

def login(request):
    return render(request,'core/login.html')

def services(request):
    return render(request,'core/services.html')

def register(request):
    return render(request,'core/forgot.html')

def forgot(request):
    return render(request,'core/forgot-username.html')

def space(request):
    return render(request,'core/space.html')

def baking(request):
    return render(request,'core/baking.html')

def collection(request):
    return render(request,'core/collection.html')

def custom(request):
    return render(request,'core/custom.html')

def social_media(request):
    return render(request,'core/social-media.html')

def confirmation(request):
    return render(request,'core/confirmation.html')







