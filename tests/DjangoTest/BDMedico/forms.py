# forms.py
from django import forms
from .models import Medicamento, Empleados, Suministro


class MedicamentoForm(forms.ModelForm):
    class Meta:
        model = Medicamento
        fields = ['name', 'descripcion', 'precio','units','LOTE','expira','marca']
        # Puedes agregar más campos según tus necesidades
        widgets = {
            'expira': forms.DateInput(attrs={'type': 'date'}),
            'units': forms.NumberInput(attrs={'type': 'number'}),
        }

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleados
        fields = ['username', 'password', 'name','surname', 'birthdate','sex',
                   'address', 'phone', 'description', 'puesto','salary'
                   , 'cedula']
        # Puedes agregar más campos según tus necesidades
        widgets = {
            'birthdate': forms.DateInput(attrs={'type': 'date'}),
            'sex': forms.Select(choices=Empleados.SEXO_CHOICES),
            'puesto': forms.Select(choices=Empleados.PUESTO_CHOICES),
        }
        
class SuministroForm(forms.ModelForm):
    class Meta:
        model = Suministro
        fields = ['name', 'descripcion', 'precio','units','LOTE','expira','desechable']
        # Puedes agregar más campos según tus necesidades
        widgets = {
            'expira': forms.DateInput(attrs={'type': 'date'}),
            'desechable': forms.CheckboxInput(),

        }