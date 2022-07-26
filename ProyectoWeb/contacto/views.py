from django.shortcuts import render, redirect
from .forms import FormularioContacto
from django.core.mail import EmailMessage


# Create your views here.


def contacto(request):
    formulario_contacto = FormularioContacto()

    if request.method == 'POST':
        formulario_contacto = FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre = request.POST.get('nombre')
            email = request.POST.get('email')
            contenido = request.POST.get('contenido')
            email = EmailMessage('Mensje desde la app django',
                                 'El usuario con nombre {} con la direccion {} escribe lo siguente: \n\n {}'.format(
                                     nombre, email, contenido),'artelec10@gmail.com')
            try:
                email.send()
                return redirect('/contacto/?valido')
            except:
                return redirect('/contacto/?novalido')

    return render(request, 'contacto/contacto.html', {'miformulario': formulario_contacto})
