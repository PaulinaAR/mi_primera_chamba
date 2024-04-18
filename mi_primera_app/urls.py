from django.urls import path
from mi_primera_app import views


urlpatterns = [
    path('', views.index),
    path('otra/', views.otra, name='otrapagina'),
    path('contacto/', views.contacto, name="contacto"),
    path('formpage/', views.form_user_view, name='form_user')
]