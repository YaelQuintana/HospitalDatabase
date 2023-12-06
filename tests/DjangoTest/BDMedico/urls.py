from django.urls import path
from .views import *

urlpatterns=[
    path('',index,name='index'),    
    path('informes/',informes,name='informes'),
    path('empleado/',empleado,name='empleado'),
    path('empleado/nuevo/',alta_empleado,name='alta_empleado'),
    path('empleado/<str:pk>/',empleado_detail,name='empleado_detail'),
    path('empleado/<str:pk>/editar/',empleado_editar,name='empleado_editar'),
    path('empleado/<str:pk>/eliminar/',empleado_eliminar,name='empleado_eliminar'),

    path('medicamento/<int:pk>/',medicamento_detail,name='medicamento_detail'),
    path('medicamento/<int:pk>/editar/', medicamento_editar, name='medicamento_editar'),
    path('medicamento/<int:pk>/eliminar/', medicamento_eliminar, name='medicamento_eliminar'),
    path('medicamento/nuevo/',alta_medicamento,name='alta_medicamento'),
    path('medicamento/',medicamento,name='medicamento'),
    ##path('side_menu/',side_menu,name='side_menu'),
    

    path('suministro/<int:pk>/',suministro_detail,name='suministro_detail'),
    path('suministro/<int:pk>/editar/', suministro_editar, name='suministro_editar'),
    path('suministro/<int:pk>/eliminar/', suministro_eliminar, name='suministro_eliminar'),
    path('suministro/nuevo/',alta_suministro,name='alta_suministro'),
    path('suministro/',suministro,name='suministro'),
    path('admin/',admin,name='admin'),

]