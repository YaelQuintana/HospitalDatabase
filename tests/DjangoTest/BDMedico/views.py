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

def staff(request):
    ##Query the database
    staff= Test.objects.all()
        # Pass data to HTML template
    context={
        'test':staff
    }
    return render(request,'BDMedico/staff.html',context)



##Testing DATA viws

# import psycopg2
# import jinja2

# # Connect to the database
# ##Se usara ese usuario y contrasenna../
# conn = psycopg2.connect(
#     database="hospitaldb",
#     user="hospitaladmin",
#     password="1234",
#     host="localhost",
#     port=5432
# )
# cursor = conn.cursor()

# # Query the database
# cursor.execute("SELECT name, status FROM staff")
# results = cursor.fetchall()

# # Pass data to HTML template
# template = jinja2.Template("""
#   <h1>Staff Status</h1>

# <table>
#   {% for row in data %}
#   <tr>
#     {% for value in row %}
#     <td>{{ value }}</td>
#     {% endfor %}
#   </tr>
#   {% endfor %}
# </table>                      
# """)

# html = template.render(data=results)

# # Print or save the HTML as needed
# # Close the database connection
# conn.close()

# def hello(request):
#     return HttpResponse(html)