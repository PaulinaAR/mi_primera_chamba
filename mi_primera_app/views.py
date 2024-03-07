from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    my_context = {'username': 'Hola desde views.py'}
    return render(request, 'mi_primera_app/index.html', context=my_context)
    #return HttpResponse("<h1>Recuerdo el día en que de la chamba yo me enamoré</h1>")