from django.urls import path
from .views import *

urlpatterns=[
    path('',index,name='index'),
    path('informes/',informes,name='informes'),
    path('staff/',staff,name='staff'),

]