from django.urls import path
from ProyectoWebApp.views import *
from django.conf import settings
from django.conf.urls.static import static
from servicios.views import servicios


urlpatterns = [
    path('', home, name='Home'),
    

]
# URL para ver las imagenes del server
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
