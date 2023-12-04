from django.db import models
# # Create your models here.
# from django_tenants.models import TenantMixin, DomainMixin

# # class Client(TenantMixin):
# #     name = models.CharField(max_length=100)
# #     paid_until =  models.DateField()
# #     on_trial = models.BooleanField()
# #     created_on = models.DateField(auto_now_add=True)

# #     # default true, schema will be automatically created and synced when it is saved
# #     auto_create_schema = True

# # class Domain(DomainMixin):
# #     pass
# class Client(TenantMixin):
#     name = models.CharField(max_length=100)
#     created_on = models.DateField(auto_now_add=True)

# class Domain(DomainMixin):
#     pass

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
    
