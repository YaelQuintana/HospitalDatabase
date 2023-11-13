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
    description=models.TextField()
    units=models.IntegerField()
    Last_Maint=models.DateField()
    
    class Meta:
        verbose_name_plural="Equipos Medicos"
        verbose_name="Equipo Medico"

    def __str__(self):
        return self.name

    @property
    def Equipo_name(self):
        return self.name

class Empleado(models.Model):
    pass

class Test(models.Model):
    name=models.TextField()
    descripcion=models.TextField()
    
