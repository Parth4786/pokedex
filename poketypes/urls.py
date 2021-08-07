from django.contrib import admin
from django.urls import path
from poketypes import views

urlpatterns = [
        path('',views.index,name ='poketypes'),
        
    
]