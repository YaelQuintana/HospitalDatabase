from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import MedicamentoForm, EmpleadoForm, SuministroForm
from datetime import date,datetime, timedelta
from django.db.models import Q

##from django.http import HttpResponse
# Create your views here.


def index(request):
    ##Here is the data that will be read
    testss=Test.objects.all()

    fechamas30=date.today()+ timedelta(days=30)
    fechamen30=date.today()- timedelta(days=30)
    medicamento = Medicamento.objects.filter(Q(expira__lte=fechamas30)| Q(units__lte=5))
    empleado= Empleados.objects.filter(contratacion_date__gte=fechamen30)
    suministro = Suministro.objects.filter(Q(expira__lte=fechamas30)| Q(units__lte=5))
    
    context={
        'empleado':empleado,
        'tests':testss,
        'caducidad':medicamento,
        'fecha_actual':fechamas30,
        'suministro':suministro,

    }
    return render(request,'index.html',context)




def informes(request):
    medicamento=Medicamento.objects.all()
    suministros=Suministro.objects.all()
    #Here the data is passed to the template
    context={
        'medicamento':medicamento,
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


# region suministro

##Detalle
def suministro_detail(request, pk):
    suministro = get_object_or_404(Suministro, pk=pk)

    # Obtener el siguiente y anterior suministro
    siguiente_suministro = Suministro.objects.filter(id__gt=suministro.id).first()
    anterior_suministro = Suministro.objects.filter(id__lt=suministro.id).last()
    
     # Formulario para la edición
    if request.method == 'POST':
        form = SuministroForm(request.POST, instance=suministro)
        if form.is_valid():
            form.save()
            return redirect('suministro_detail', pk=pk)
    else:
        form = SuministroForm(instance=suministro)

    return render(request, 'Suministro/suministro_detail.html', {
        'suministro': suministro,
        'form': form,
        'siguiente_suministro': siguiente_suministro,
        'anterior_suministro': anterior_suministro,
    })


##Lista Todos los suministros de la BD
def suministro(request):
    ##Query the database
    suministros= Suministro.objects.all()
        # Pass data to HTML template
    context={
        'suministro':suministros
    }
    return render(request,'Suministro/suministro.html',context)

##Alta suministro
def alta_suministro(request):
    if request.method == 'POST':
        form = SuministroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('suministro')  # Redirige a la página de lista de suministros
    else:
        form = SuministroForm()
    return render(request, 'Suministro/suministro_alta.html', {'form': form})

##Edita suministro
def suministro_editar(request, pk):
    suministro = get_object_or_404(Suministro, pk=pk)

    # Obtener el siguiente y anterior suministro
    siguiente_suministro = Suministro.objects.filter(id__gt=suministro.id).first()
    anterior_suministro = Suministro.objects.filter(id__lt=suministro.id).last()
    
    form = SuministroForm(instance=suministro)

    return render(request, 'Suministro/suministro_edita.html', {
        'suministro': suministro,
        'form': form,
        'siguiente_suministro': siguiente_suministro,
        'anterior_suministro': anterior_suministro,
    })
    ##Baja suministro
def suministro_eliminar(request, pk):
    suministro = get_object_or_404(Suministro, id=pk)
    suministro.delete()
    return redirect('suministro')  # Redirige a la página de lista de suministros
    


# endregion

