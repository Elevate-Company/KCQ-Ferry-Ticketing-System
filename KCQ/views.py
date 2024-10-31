# backend/KCQ/views.py
from django.shortcuts import render

def frontend(request):
    return render(request, 'index.html')  # This is the index.html in the build folder
