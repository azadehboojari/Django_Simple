from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

def index(request):
    if "counter" in request.session:
        request.session["counter"]+=1
    else:
        request.session["counter"]=1
    context={
    'word': get_random_string(length=14)
     }
    return render ( request,'word_app/index.html', context)

def attempt(request):
    return (redirect('/'))
def reset (request):
    request.session.clear()
    return (redirect('/'))
    

