# Generated by Django 4.2.7 on 2023-12-04 04:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BDMedico', '0006_remove_empleado_id_empleado_address_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Empleado',
            new_name='Empleados',
        ),
    ]
