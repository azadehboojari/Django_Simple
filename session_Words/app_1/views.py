from django.shortcuts import render, redirect
from datetime import datetime

def index(request):
    if 'words' not in request.session:
        request.session['words']=[]
    return render (request, 'app_1/index.html')

def add(request):
    word = {
        "word": request.POST["word"],
        "time": datetime.now().strftime("%I:%M:%S %p, %B %dth %Y")
    }
    if "color" in request.POST:
        word["color"] = request.POST["color"]
    else:
        word["color"] = "black"
    if "font" in request.POST:
        word["font"] = request.POST["font"]
    else:
        word["font"] = "regular"
    print(word)
    request.session["words"].append(word)
    print(request.session["words"])
    request.session.modified = True
    return redirect("/")

def clear(req):
    req.session.clear()
    return redirect("/")

