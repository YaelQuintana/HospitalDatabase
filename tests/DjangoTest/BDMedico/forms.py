# forms.py
from django import forms
from .models import Medicamento, Empleados


class MedicamentoForm(forms.ModelForm):
    class Meta:
        model = Medicamento
        fields = ['name', 'descripcion', 'precio','units','LOTE','expira']
        # Puedes agregar más campos según tus necesidades

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleados
        fields = ['username', 'password', 'name','surname', 'birthdate','sex',
                   'address', 'phone', 'description', 'puesto','salary'
                   , 'cedula']
        # Puedes agregar más campos según tus necesidades
        