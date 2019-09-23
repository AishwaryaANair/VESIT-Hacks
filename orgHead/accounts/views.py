from django.shortcuts import render
from .models import Teams

# Create your views here.

def login(request):
    return render(request,'accounts/signandsignup.html')

def home(request): 
    teams = Teams.objects.all()
    return render(request,'home.html',{'teams':teams})
    
def emp(request):
    username = Profile.objects.all()  
    return render(request,'accounts/emp.html',{'username':username})

def rating(request):
    return render(request,'accounts/ratingForm.html')

def projectForm(request):
    
    return render(request,'accounts/projectForm.html')

def teamLeader(request):
    titles = Projects.object.all()
    return render(request,'accounts/Team_leader.html',{'titles':titles})