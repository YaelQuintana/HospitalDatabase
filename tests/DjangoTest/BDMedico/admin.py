from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Medicamento)
class Medicamentdmin(admin.ModelAdmin):
    list_display=('name',)

@admin.register(Suministro)    
class SuministroAdmin(admin.ModelAdmin):
    list_display=('name',)

@admin.register(Equipo_Med)    
class Equipo_MedAdmin(admin.ModelAdmin):
    list_display=('name',)

@admin.register(Test)    
class TestAdmin(admin.ModelAdmin):
    list_display=('name',)