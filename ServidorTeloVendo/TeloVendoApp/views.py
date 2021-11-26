from django.shortcuts import redirect, render
from .models import Cliente
from .forms import ProveedorForm


# Create your views here.

def index(request):
    return render(request, 'TeloVendoApp/index.html')

def base_cliente(request):
    cliente = Cliente.objects.all()
    return render(request, 'TeloVendoApp/base_cliente.html',{'data': cliente})

# def base_proveedor(request):
#     if request.method == "POST":
#         form = Proveedores(data = request.POST)
#         rut = form["rut"]
#         nombre_proveedor = form["nombre_proveedor"]
#         direccion = form["direccion"]
#         contacto_telefonico = form["contacto_telefonico"]
#         email = form["email"]
#         producto = form["producto"]
#         if form.is_valid():
#             proveedor = form.save(commit = False)
#             proveedor.save()
#         return redirect('/proveedor')
#     else:
#         form = Proveedores()
#         return render(request,'TeloVendoApp/formulario_proveedores.html', {"form": form})

def base_proveedor(request):
    if request.method == "POST":
        form = ProveedorForm(data = request.POST)
        if form.is_valid():
            proveedor = form.save(commit = False)
            proveedor.save()
        return redirect('/base_cliente')
    else:
        form = ProveedorForm()
        return render(request,'TeloVendoApp/formulario_proveedores.html', {"form": form})