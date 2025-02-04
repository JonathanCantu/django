from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    template = "main/index.html"
    return render(request, template)

def detail(request):
    return HttpResponse("Welcome to App 1 Detail Page")

