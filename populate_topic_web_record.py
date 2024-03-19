import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mi_primera_chamba.settings')

import django
django.setup()

# Configuraciones generales
import random
from mi_primera_app.models import Topic, Webpage, AccessRecord
from faker import Faker

faker_generator = Faker()
topics = ['Videojuegos', 'Noticias', 'Streaming', 'Negocios', 'Buscador', 'Red social', 'Correo']

#Añadir tematicas
def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0] #Solamente se requiere el primer elemento de la tupla
    t.save()
    return t

#Poblar las tablas
def populate(N=5):
    for entry in range(N):
        top = add_topic()
        #Crear datos falsos
        fake_name = faker_generator.company()
        fake_url = faker_generator.url()
        fake_date = faker_generator.date()

        #Crear pagina ficticia en el modelo
        webpage = Webpage.objects.get_or_create(topic=top, name=fake_name, url=fake_url)[0]

        #Crear Access Record ficticio
        acc_record = AccessRecord.objects.get_or_create(webname=webpage, date=fake_date)[0]


if __name__ == '__main__':
    print("Comienzo a poblar")
    populate(20)
    print("Ya estuvo")