from django.urls import path
from contacto.views import contacto
from django.conf.urls.static import static


urlpatterns = [
    path('', contacto, name='Contacto'),
]

