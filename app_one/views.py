from django.shortcuts import redirect, render, HttpResponse

def index(request):
    return HttpResponse("placeholder later to display a list of all blogs")
# Create your views here.
def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

def create(request):
    return redirect("/")

def show(request, number):
    return HttpResponse(f"placeholder to display a blog number: {number}")

def edit(request, number):
    return HttpResponse(f"placeholder to edit blog number: {number}")

def destroy(request, number):
    return redirect("/")