from django.urls import path
from autenticacion.views import VRegistro, cerrar_sesion,loggin



urlpatterns = [
    path('', VRegistro.as_view(), name='Autenticacion'),
    path('cerrar_sesion', cerrar_sesion, name='cerrar_sesion'),
    path('login', loggin, name='login'),
]


