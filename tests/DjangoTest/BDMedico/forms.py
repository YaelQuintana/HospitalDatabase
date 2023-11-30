# forms.py
from django import forms
from .models import Medicamento

class MedicamentoForm(forms.ModelForm):
    class Meta:
        model = Medicamento
        fields = ['name', 'descripcion', 'precio','units','LOTE','expira']
        # Puedes agregar más campos según tus necesidades
