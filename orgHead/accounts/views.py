from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request,'accounts/signandsignup.html')

def home(request): 
    return render(request,'home.html')
    
def emp(request):
    return render(request,'accounts/emp.html')

def rating(request):
    return render(request,'accounts/ratingForm.html')

def projectForm(request):
    return render(request,'accounts/projectForm.html')

def teamLeader(request):
    return render(request,'accounts/Team_leader.html')