from django.http import response,HttpRequest,HttpResponse,JsonResponse
from django.shortcuts import render
import requests

def index(request):
    r = requests.get("https://pokeapi.co/api/v2/type/") #request the data from pokeapi 
    return JsonResponse(r.json()) #it returns the data on our site in json format
   


   
  