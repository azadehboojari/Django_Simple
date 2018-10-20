from django.shortcuts import render, redirect
from models import Author


def index(request):
    context = {"authors": Author.objects.all()}
    return render(request, "app_1index.html", context)

def result(request):
    return render (request, 'app_1/result.html')