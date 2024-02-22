from django.shortcuts import render, redirect
from . forms import CreateUserForm
# Create your views here.
def index(request):
    return render(request,'core/index.html')

def login(request):
    return render(request,'core/login.html')

def services(request):
    return render(request,'core/services.html')

def register(request):        
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("http://127.0.0.1:8000/login/")

            
    
    
    
    context = {'registerform': form}
    
    return render(request, 'core/register.html',context= context)

 







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





