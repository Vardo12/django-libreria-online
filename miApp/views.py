from django.shortcuts import render, get_object_or_404
from .models import Producto, Categoria

def home(request):
    productos = Producto.objects.all()
    categorias = Categoria.objects.all()
    return render(request, 'home.html', {'productos': productos, 'categorias': categorias})

def categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    productos = Producto.objects.filter(categoria=categoria)
    return render(request, 'categoria.html', {'categoria': categoria, 'productos': productos})

def detalle(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    return render(request, 'detalle.html', {'producto': producto})
    