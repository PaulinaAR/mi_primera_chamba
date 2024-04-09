from django.shortcuts import render
from django.http import HttpResponse
from mi_primera_app.models import Topic, Webpage, AccessRecord, ElProfe
from . import forms

# Create your views here.
def index(request):
    access_list = AccessRecord.objects.order_by('date')
    elprofe_list = ElProfe.objects.order_by('email')
    my_context = {'username': 'Hola desde views.py',
                  'access_records': access_list,
                  'el_profe': elprofe_list}
    return render(request, 'mi_primera_app/index.html', context=my_context)
    #return HttpResponse("<h1>Recuerdo el día en que de la chamba yo me enamoré</h1>")

#Crear un formulario para mostrar
def form_user_view(request):
    form = forms.FormUser()
    return render(request, 'mi_primera_app/form_page.html', {'form' : form})