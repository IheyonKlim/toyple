from django.shortcuts import render

def index(request):
    return render(request, 'templates/index.html')


def other(request):
    return render(request, 'templates/other.html')


