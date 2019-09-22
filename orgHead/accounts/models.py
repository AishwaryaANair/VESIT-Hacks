from django.db import models
from django.contrib.auth.models import User

from enum import Enum
from datetime import date

# Create your models here.
class PositionChoice(Enum): 
    EMP = "Employee"
    TL = "Team Leader"
    FM = "Manager"
    HS = "Head Supervisor"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    type = models.TextField(max_length=500)
    teamName = models.ForeignKey(Team, on_delete = models.SET_NULL)
    position = models.CharField(
    max_length=20,
      choices=[(tag, tag.value) for tag in PositionChoice]  # Choices is a list of Tuple
    )
    
class Projects(models.Model):
    title = models.CharField(max_length=20),
    desc = models.TextField(),
    deadline = models.DateField(_("Date"), default=datetime.date.today)
    