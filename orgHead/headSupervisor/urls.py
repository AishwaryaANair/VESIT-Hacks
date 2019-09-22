from django.urls import path, include
from django.contrib.auth import views

urlpatterns = [
    path('',views.admin,name='admin'),
]
