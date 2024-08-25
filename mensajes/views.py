from django.shortcuts import render
from .models import Mensaje

def mensajes_recibidos(request):
    # Obtener el destinatario 
    destinatario = request.GET.get('destinatario', '')

    # Filtrar los mensajes que tienen el destinatario 
    if destinatario:
        mensajes = Mensaje.objects.filter(destinatario=destinatario)
    else:
        mensajes = Mensaje.objects.none()  

   
    return render(request, 'recibidos.html', {'mensajes': mensajes})
