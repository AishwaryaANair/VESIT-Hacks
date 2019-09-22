from django.urls import path,re_path
from . import views

urlpatterns = [
    path('',views.amit,name = 'headSupervisor'),
    path('teamProgress',views.teamProgress,name='teamProgress'),
<<<<<<< Updated upstream
    path('teamPStructure',views.teamStructure,name='teamStructure')
=======
    path('teamStructure',views.teamStructure,name='teamStructure')
>>>>>>> Stashed changes
]