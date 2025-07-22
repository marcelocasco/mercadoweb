from django.shortcuts import render

def producto(request):
    return render(request, 'producto.html')

def producto_limpieza(request):
    return render(request, 'producto_limpieza.html')
