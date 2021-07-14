from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request):
    return render(request,"generator/home.html",{"password":"fasfdsfgasg"})

def password(request):
    thePassword=""
    characters=list("abcdefghijklmnopqrstuvwxyz")
    length=int(request.GET.get("length",12))
    if request.GET.get("upperCase"):
        characters.extend(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    if request.GET.get("numbers"):
        characters.extend(list("0123456789"))
    if request.GET.get("specialCharacters"):
        characters.extend(list("!@#$%^&*()"))
    for i in range(length):
        thePassword+=random.choice(characters)
    return render (request,"generator/password.html",{"password":thePassword})

def about(request):
    return render(request,"generator/about.html")
