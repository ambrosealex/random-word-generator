from django.shortcuts import render, redirect
import string
import random

# Create your views here.
def index(request):
    if "count" not in request.session:
        request.session["count"] = 0
    return render(request, "randomword/index.html")

def generate(request):
    print request.method
    if request.method == "POST":
        request.session["count"] = request.session["count"] + 1
        request.session["word"] = ""
        for i in range(0,14):
            request.session["word"] += random.choice(string.letters)
        request.session["word"] = request.session["word"].lower()
        return redirect('/')
    else:
        return redirect('/')
