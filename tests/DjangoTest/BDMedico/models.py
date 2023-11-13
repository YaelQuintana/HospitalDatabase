from django.db import models

# Create your models here.
class Medicamento(models.Model):
    name=models.CharField(max_length=255)
    descripcion=models.TextField()
    units=models.IntegerField()
    precio=models.DecimalField(decimal_places=2,max_digits=10)
    LOTE=models.CharField(max_length=20)
    expira=models.DateField()


class Suministro(models.Model):
    name=models.CharField(max_length=255)
    descripcion=models.TextField()
    units=models.IntegerField()
    precio=models.DecimalField(decimal_places=2, max_digits=10)
    LOTE=models.CharField(max_length=20)
    expira=models.DateField()
    desechable=models.BooleanField(default=True)



class Equipo_Med(models.Model):
    name=models.CharField(max_length=255)
    descripcion=models.TextField()
    units=models.IntegerField()
    Last_Maint=models.DateField()

class Empleado(models.Model):
    pass

