from django.shortcuts import render, redirect, get_object_or_404
from .models import *
##from django.http import HttpResponse
# Create your views here.
def index(request):
    ##Aqui va los datos que leeera
    testss=Test.objects.all()
    context={
        'tests':testss
    }
    return render(request,'BDMedico/index.html',context)

def informes(request):
    equipos=Equipo_Med.objects.all()
    suministros=Suministro.objects.all()
    #Aqui se le pasan los datos al template
    context={
        'equipos':equipos,
        'suministros':suministros
    }
    return render(request,'BDMedico/informes.html',context)

def medicamento_detail(request, pk):
    medicamento = Medicamento.objects.get(id=pk)
    # Fetch the object related to passed id
    context = {
        'medicamento': medicamento
    }
    return render(request,'BDMedico/medicamento_detail.html', context)

def medicamento(request):
    ##Query the database
    medicamentos= Medicamento.objects.all()
        # Pass data to HTML template
    context={
        'medicamento':medicamentos
    }
    return render(request,'BDMedico/medicamento.html',context)
def staff(request):
    ##Query the database
    staff= Test.objects.all()
        # Pass data to HTML template
    context={
        'staff':staff
    }
    return render(request,'BDMedico/staff.html',context)

