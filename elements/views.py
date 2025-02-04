from django.shortcuts import render
#from django.http import HttpResponse
from elements.models import Elements

def index(request):
    template = "main/index.html"

    elements = Elements.objects.all()
    context = {
        'elements': elements
    }

    return render(request, template, context)

