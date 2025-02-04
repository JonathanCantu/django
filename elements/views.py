from django.shortcuts import render
from django.http import HttpResponse
from elements.models import Elements

def index(request):
    begin_table = "<table border='2'>"

    caption = "<caption>Periodic Table of the Elements</caption>"

    header = "<tr><th>AtomicNumber</th><th>Element</th><th>Symbol</th><th>AtomicMass</th></tr>"

    elements = Elements.objects.all()

    row = " "

    for e in elements:
        row = f"{row}<tr><td>{e.atomic_number}</td><td>{e.element}</td><td>{e.symbol}</td><td>{e.atomic_mass}</td></tr>"
        
    end_table = "</table>"

    response = f"<html><body><img src='{% static 'images/atom-electrons.gif' %}' class='animated-atom' style='width:120px; margin-bottom:-50px;'>{begin_table}\n{caption}\n{header}\n{row}\n{end_table}\n</body></html>"

    return HttpResponse(response)

