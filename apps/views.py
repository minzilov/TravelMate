from django.shortcuts import render

# Create your views here.

def opening(request):
    return render(request, 'opening.html')

def diary(request):
    return render(request, 'diary.html')

def map(request):
    return render(request, 'map.html')

