from django.db import models
from django.core.validators import RegexValidator


# Create your models here.
class Medicamento(models.Model):
    name = models.CharField(max_length=255)
    descripcion = models.TextField()
    precio = models.DecimalField(decimal_places=2, max_digits=10)
    units = models.IntegerField()
    LOTE = models.CharField(max_length=20, unique=True)
    expira = models.DateField()
    marca = models.CharField(max_length=255, default='Generico')

    def __str__(self):
        return self.name




class Suministro(models.Model):
    name=models.CharField(max_length=255)
    descripcion=models.TextField()
    units=models.IntegerField()
    precio=models.DecimalField(decimal_places=2, max_digits=10)
    LOTE=models.CharField(max_length=20)
    expira=models.DateField(null=True)
    desechable=models.BooleanField(default=True)



    

class Empleados(models.Model):
    username = models.CharField(max_length=50, primary_key=True)
    password=models.CharField(max_length=50)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    birthdate = models.DateField()
    sex = models.CharField(max_length=20)
    address = models.CharField(max_length=255, default="")
    description = models.TextField()
    puesto = models.CharField(max_length=255)
    salary = models.DecimalField(decimal_places=2, max_digits=10)
    contratacion_date = models.DateTimeField(auto_now_add=True, blank=True)
    cedula = models.CharField(max_length=255,unique=True)


    phone = models.CharField(
        max_length=20,
        unique=True, 
        validators=[RegexValidator(regex=r'^[0-9#+]*$', message='Solo se permiten números, letras, "#" y "+"')],
   
    )

    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro'),
    ]
    sex = models.CharField(max_length=1, choices=SEXO_CHOICES)


    PUESTO_CHOICES = [
        ('admin', 'Administrador'),
        ('empleado', 'Empleado'),
        ('medico', 'Medico'),
        ('recepcionista', 'Recepcionista'),
        ('farmaceutico', 'Farmaceutico'),
        ('enfermeria', 'Enfermeria'),
        ('jardinero', 'Jardinero'),
        ('gerente', 'Gerente'),
        ('supervisor', 'Supervisor'),
        ('tecnico', 'Técnico'),
        ('asistente', 'Asistente'),
        ('auxiliar', 'Auxiliar'),
        ('conserje', 'Conserje'),
        ('otro', 'Otro'),

        # Agregar más opciones si así se requiere
    ]
    puesto = models.CharField(max_length=20, choices=PUESTO_CHOICES)
    def __str__(self):
        return self.name
    


class Entradas(models.Model):
    count=models.AutoField(primary_key=True)
    user=models.ForeignKey(Empleados, on_delete=models.CASCADE, null=True, blank=True)
    dateentry = models.DateTimeField(auto_now_add=True, blank=True)


    
class Test(models.Model):
    name=models.TextField()
    descripcion=models.TextField()
    
