from django.shortcuts import render
from accounts.models import *

# Create your views here.
def amit(request):
    return render(request,'teamDash/teamDash.html')
    
def teamProgress(request):
    return render(request,'accounts/teamProgress.html')
 
def teamStructure(request):
    
    return render(request,'accounts/teamStructure.html')

