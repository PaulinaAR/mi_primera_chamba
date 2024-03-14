from django.contrib import admin
from mi_primera_app.models import Topic, Webpage, AccessRecord

# Register your models here.
admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(AccessRecord)