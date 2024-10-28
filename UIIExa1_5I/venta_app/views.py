from django.shortcuts import render
from .models import Venta
# Create your views here.
def inicio_vista(request):
    # obtener todos los registros de la tabla
    ListadoVentas=Venta.objects.all()
    return render(request,"gestionarVentas.html",{"lasventas":ListadoVentas})