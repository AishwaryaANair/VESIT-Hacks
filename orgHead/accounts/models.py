from django.db import models
from django.contrib.auth.models import User

from enum import Enum
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
    
    