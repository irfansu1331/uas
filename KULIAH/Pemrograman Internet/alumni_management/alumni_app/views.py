from django.shortcuts import render

def home(request):
    return render(request, 'alumni_management/home.html')
