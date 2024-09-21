from django.shortcuts import render

def home_view(request):
    return render(request, 'home/index.html')

def login_view(request):
    return render(request, 'home/login.html')