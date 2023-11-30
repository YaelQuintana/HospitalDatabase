from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import MedicamentoForm

##from django.http import HttpResponse
# Create your views here.


def index(request):
    ##Here is the data that will be read
    testss=Test.objects.all()
    context={
        'tests':testss
    }
    return render(request,'BDMedico/index.html',context)

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

    return render(request, 'BDMedico/medicamento_detail.html', {
        'medicamento': medicamento,
        'form': form,
        'siguiente_medicamento': siguiente_medicamento,
        'anterior_medicamento': anterior_medicamento,
    })


    # Pass data to HTML template
    # Fetch the object related to passed id
    # context = {
    #     'medicamento': medicamento
    # }
    # return render(request,'BDMedico/medicamento_detail.html', context)

##Lista Todos los medicamentos de la BD
def medicamento(request):
    ##Query the database
    medicamentos= Medicamento.objects.all()
        # Pass data to HTML template
    context={
        'medicamento':medicamentos
    }
    return render(request,'BDMedico/medicamento.html',context)

##Alta Medicamento
def alta_medicamento(request):
    if request.method == 'POST':
        form = MedicamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('medicamento')  # Redirige a la página de lista de medicamentos
    else:
        form = MedicamentoForm()

    return render(request, 'BDMedico/medicamento_alta.html', {'form': form})

##Edita Medicamento
def edita_medicamento(request, pk):
    medicamento = get_object_or_404(Medicamento, id=pk)
    if request.method == 'POST':
        form = MedicamentoForm(request.POST, instance=medicamento)
        if form.is_valid():
            form.save()
            return redirect('medicamento')  # Redirige a la página de lista de medicamentos
    else:
        form = MedicamentoForm(instance=medicamento)
        return render(request,'medicamento_edita.html', {'form': form})
    
    ##Baja Medicamento
def baja_medicamento(request, pk):
    medicamento = get_object_or_404(Medicamento, id=pk)
    if request.method == 'POST':
        medicamento.delete()
        return redirect('medicamento')  # Redirige a la página de lista de medicamentos
    else:
        return render(request,'medicamento_baja.html', {'medicamento': medicamento})


# endregion



def staff(request):
    ##Query the database
    staff= Test.objects.all()
        # Pass data to HTML template
    context={
        'staff':staff
    }
    return render(request,'BDMedico/staff.html',context)

