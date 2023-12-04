from django.db import models
from django.utils.timezone import now


# Create your models here.
class Medicamento(models.Model):
    name=models.CharField(max_length=255)
    descripcion=models.TextField()
    units=models.IntegerField()
    precio=models.DecimalField(decimal_places=2,max_digits=10)
    LOTE=models.CharField(max_length=20)
    expira=models.DateField()

    def __str__(self):
        return self.name


class Suministro(models.Model):
    name=models.CharField(max_length=255)
    descripcion=models.TextField()
    units=models.IntegerField()
    precio=models.DecimalField(decimal_places=2, max_digits=10)
    LOTE=models.CharField(max_length=20)
    expira=models.DateField()
    desechable=models.BooleanField(default=True)



class Equipo_Med(models.Model):
    id=models.AutoField(primary_key=True)
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
    

class Empleados(models.Model):
    username = models.CharField(max_length=50, primary_key=True)
    password=models.CharField(max_length=50)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    birthdate = models.DateField()
    sex = models.CharField(max_length=10)
    address = models.CharField(max_length=255, default="")
    phone = models.CharField(max_length=20, unique=True)
    description = models.TextField()
    puesto = models.CharField(max_length=255)
    salary = models.DecimalField(decimal_places=2, max_digits=10)
    contratacion_date = models.DateTimeField(auto_now_add=True, blank=True)
    cedula = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    


class Entradas(models.Model):
    count=models.AutoField(primary_key=True)
    user=models.ForeignKey(Empleados, on_delete=models.CASCADE, null=True, blank=True)
    dateentry = models.DateTimeField(auto_now_add=True, blank=True)


    
class Test(models.Model):
    name=models.TextField()
    descripcion=models.TextField()
    
