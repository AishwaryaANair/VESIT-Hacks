from django.db import models
from django.contrib.auth.models import User
from django.utils import datetime_safe
from enum import Enum
from datetime import date

# Create your models here.
class PositionChoice(Enum): 
    EMP = "Employee"
    TL = "Team Leader"
    FM = "Manager"
    HS = "Head Supervisor"

class Teams(models.Model):
    teamName = models.CharField(max_length = 200)
    teamLeader =  models.OneToOneField(User, on_delete = models)
    time = models.DateTimeField(default = date.today)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    type = models.TextField(max_length=500)
    teamId = models.ForeignKey(Teams, on_delete = models.SET_NULL)
    position = models.CharField(
    max_length=20,
      choices=[(tag, tag.value) for tag in PositionChoice]  # Choices is a list of Tuple
    )


class Projects(models.Model):
    teamid = models.ForeignKey(
      Teams,on_delete = models.CASCADE),
    title = models.CharField(max_length=20),
    desc = models.TextField(),
<<<<<<< HEAD
    deadline = models.DateField(default=date.today)

class ProjectReport(models.Model):
    teamid = models.ForeignKey(
      Teams,on_delete = models.CASCADE),
    time = models.DateField(default=date.today),
=======
    deadline = models.DateField(("Date"), default=date.today)
    


class ProjectReport(models.Model):
    teamid = models.ForeignKey(
     Teams,on_delete = models.CASCADE),
    time = models.DateField(("Date"), default=date.today),
>>>>>>> master
    pid = models.ForeignKey(
          Projects,on_delete=models.CASCADE)

    
class UserReport(models.Model):
    time = models.DateField(("Date"), default = date.today)
    projectid= models.ForeignKey(
        Projects, on_delete=models.CASCADE)
    empid= models.ForeignKey(
        User, on_delete=models.CASCADE)
    teamid= models.ForeignKey(
        Teams, on_delete=models.CASCADE)
    


    
