from django.shortcuts import render

# Create your views here.

def opening(request):
    return render(request, 'opening.html')


