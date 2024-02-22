from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'core/index.html')

def login(request):
    return render(request,'core/login.html')

def services(request):
    return render(request,'core/services.html')

def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        # Check if passwords match
        if pass1 != pass2:
            messages.error(request, "Passwords do not match.")
            return redirect('register/')

        # Check if username exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect('register/')

        # Check if email exists
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
            return redirect('register/')

        # Create user
        myuser = User.objects.create_user(username=username, email=email, password=pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()

        messages.success(request, "Your account has been successfully created.")
        return redirect('login')
        
    return render(request, 'core/register.html')

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

def news(request):
    return render(request,'core/news.html')

def about(request):
    return render(request,'core/about.html')

def contact(request):
    return render(request,'core/contact.html')

def logout(request):
    return render(request,'core/logout.html')





