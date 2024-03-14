from django.shortcuts import render
from django.http import HttpResponse
from mi_primera_app.models import Topic, Webpage, AccessRecord

# Create your views here.
def index(request):
    access_list = AccessRecord.objects.order_by('date')
    my_context = {'username': 'Hola desde views.py',
                  'access_records': access_list}
    return render(request, 'mi_primera_app/index.html', context=my_context)
    #return HttpResponse("<h1>Recuerdo el día en que de la chamba yo me enamoré</h1>")