from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request,'accounts/signandsignup')

def home(request): 
    return render(request,'home.html')
    
