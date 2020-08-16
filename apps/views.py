from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def diary(request):
    return render(request, 'diary.html')

def map(request):
    return render(request, 'map.html')

