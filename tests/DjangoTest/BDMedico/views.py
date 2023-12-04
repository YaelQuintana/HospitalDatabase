from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import MedicamentoForm, EmpleadoForm

##from django.http import HttpResponse
# Create your views here.


def index(request):
    ##Here is the data that will be read
    testss=Test.objects.all()
    context={
        'tests':testss
    }
    return render(request,'index.html',context)

def informes(request):
    equipos=Equipo_Med.objects.all()
    suministros=Suministro.objects.all()
    #Here the data is passed to the template
    context={
        'equipos':equipos,
        'suministros':suministros
    }
    return render(request,'BDMedico/informes.html',context)

# region Medicamento

##Detalle
def medicamento_detail(request, pk):
    medicamento = get_object_or_404(Medicamento, pk=pk)

    # Obtener el siguiente y anterior medicamento
    siguiente_medicamento = Medicamento.objects.filter(id__gt=medicamento.id).first()
    anterior_medicamento = Medicamento.objects.filter(id__lt=medicamento.id).last()
    
     # Formulario para la edición
    if request.method == 'POST':
        form = MedicamentoForm(request.POST, instance=medicamento)
        if form.is_valid():
            form.save()
            return redirect('medicamento_detail', pk=pk)
    else:
        form = MedicamentoForm(instance=medicamento)

    return render(request, 'Medicamento/medicamento_detail.html', {
        'medicamento': medicamento,
        'form': form,
        'siguiente_medicamento': siguiente_medicamento,
        'anterior_medicamento': anterior_medicamento,
    })


##Lista Todos los medicamentos de la BD
def medicamento(request):
    ##Query the database
    medicamentos= Medicamento.objects.all()
        # Pass data to HTML template
    context={
        'medicamento':medicamentos
    }
    return render(request,'Medicamento/medicamento.html',context)

##Alta Medicamento
def alta_medicamento(request):
    if request.method == 'POST':
        form = MedicamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('medicamento')  # Redirige a la página de lista de medicamentos
    else:
        form = MedicamentoForm()

    return render(request, 'Medicamento/medicamento_alta.html', {'form': form})

##Edita Medicamento
def medicamento_editar(request, pk):
    medicamento = get_object_or_404(Medicamento, pk=pk)

    # Obtener el siguiente y anterior medicamento
    siguiente_medicamento = Medicamento.objects.filter(id__gt=medicamento.id).first()
    anterior_medicamento = Medicamento.objects.filter(id__lt=medicamento.id).last()
    
    form = MedicamentoForm(instance=medicamento)

    return render(request, 'Medicamento/medicamento_edita.html', {
        'medicamento': medicamento,
        'form': form,
        'siguiente_medicamento': siguiente_medicamento,
        'anterior_medicamento': anterior_medicamento,
    })
    ##Baja Medicamento
def medicamento_eliminar(request, pk):
    medicamento = get_object_or_404(Medicamento, id=pk)
    medicamento.delete()
    return redirect('medicamento')  # Redirige a la página de lista de medicamentos
    


# endregion


# region Empleado

##Detalle
def empleado_detail(request, pk):
    empleado = get_object_or_404(Empleados, pk=pk)

    # Obtener el siguiente y anterior empleado
    siguiente_empleado = Empleados.objects.filter(username__gt=empleado.username).order_by('username').first()
    anterior_empleado = Empleados.objects.filter(username__lt=empleado.username).order_by('-username').first()
    
    # Formulario para la edición
    if request.method == 'POST':
        form = EmpleadoForm(request.POST, instance=empleado)
        if form.is_valid():
            # Excluye el campo 'username' para evitar que se edite
            form.fields['username'].widget.attrs['readonly'] = True
            form.save()
            return redirect('empleado_detail', pk=pk)
    else:
        form = EmpleadoForm(instance=empleado)
        # Excluye el campo 'username' para evitar que se edite
        form.fields['username'].widget.attrs['readonly'] = True

    return render(request, 'Empleado/empleado_detail.html', {
        'empleado': empleado,
        'form': form,
        'siguiente_empleado': siguiente_empleado,
        'anterior_empleado': anterior_empleado,
    })


def empleado(request):
    ##Query the database
    empleado= Empleados.objects.all()
        # Pass data to HTML template
    context={
        'empleado':empleado
    }
    return render(request,'Empleado/staff.html',context)

##Alta staff
def alta_empleado(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():

            username = form.cleaned_data['username'].lower()
            password = form.cleaned_data['password'].lower()
            form.save()
            return redirect('empleado')  # Redirige a la página de lista de empleados
    else:
        form = EmpleadoForm()
    return render(request, 'Empleado/empleado_alta.html', {'form': form})

##Edita empleado
def empleado_editar(request, pk):
    empleado = get_object_or_404(Empleados, pk=pk)

   # Obtener el siguiente y anterior empleado
    siguiente_empleado = Empleados.objects.filter(username__gt=empleado.username).order_by('username').first()
    anterior_empleado = Empleados.objects.filter(username__lt=empleado.username).order_by('-username').first()
      
    form = EmpleadoForm(instance=empleado)

    return render(request, 'Empleado/empleado_edita.html', {
        'empleado': empleado,
        'form': form,
        'siguiente_empleado': siguiente_empleado,
        'anterior_empleado': anterior_empleado,
    })
    ##Baja empleado
def empleado_eliminar(request, pk):
    empleado = get_object_or_404(Empleados, username=pk)
    empleado.delete()
    return redirect('empleado')  # Redirige a la página de lista de empleados
    
# endregion

