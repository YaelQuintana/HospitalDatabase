from django.urls import path
from .views import *

urlpatterns=[
    path('',index,name='index'),
    path('informes/',informes,name='informes'),
    path('staff/',staff,name='staff'),
    path('medicamento/<int:pk>/',medicamento_detail,name='medicamento_detail'),
    path('medicamento/<int:pk>/editar/', medicamento_editar, name='medicamento_editar'),
    path('medicamento/',medicamento,name='medicamento'),
    path('alta_medicamento/',alta_medicamento,name='alta_medicamento'),
    ##path('side_menu/',side_menu,name='side_menu'),
    
]