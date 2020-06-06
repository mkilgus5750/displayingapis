from django.shortcuts import render, HttpResponse
import requests

def index(request):
    r = requests.get("https://superheroapi.com/api/2609165169357640/620/biography")
    name = r.json()['name']
    aliases = r.json()['aliases']
    return render(request, "index.html", context={'aliases': aliases, 'name': name})
