from django.shortcuts import render, redirect
from .models import Secret, Like

def index(request):
    return render(request, 'secrets/index.html', { "secrets" : Secret.objects.all() } )

def addSecret(request):
    Secret.objects.create(secret = request.POST['secret'])
    return redirect('/')

def addLike(request, secretID):
    Like.objects.create(secret = Secret.objects.get(id = secretID))
    return redirect('/')
