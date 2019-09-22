from django.shortcuts import render

# Create your views here.
def amit(request):
    return render(request,'teamDash/teamDash.html')

def teamProgress(request):
    return render(request,'teamDash/teamProgress.html')

def teamStructure.html(request):
    return render(request,'teamDash/teamStructure.html')
