from django.shortcuts import render

def menu_geral(request):
    return render(request, 'menu_geral/menu.html')