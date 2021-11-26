from django import forms
from django.db.models import fields
from .models import Proveedor

# class Proveedores(forms.Form):
#     rut = forms.CharField(widget= forms.TextInput)
#     nombre_proveedor = forms.CharField(widget= forms.TextInput)
#     direccion = forms.CharField(widget= forms.TextInput)
#     contacto_telefonico = forms.CharField(widget= forms.TextInput)
#     email = forms.CharField(widget= forms.EmailInput)
#     producto = forms.CharField(widget= forms.TextInput)

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ('rut','nombre_proveedor','direccion','contacto_telefonico','email', 'producto')