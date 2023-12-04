# Generated by Django 4.2.8 on 2023-12-04 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BDMedico', '0009_alter_suministro_expira'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleados',
            name='puesto',
            field=models.CharField(choices=[('admin', 'Administrador'), ('empleado', 'Empleado'), ('medico', 'Medico'), ('recepcionista', 'Recepcionista'), ('farmaceutico', 'Farmaceutico'), ('enfermeria', 'Enfermeria'), ('jardinero', 'Jardinero'), ('gerente', 'Gerente'), ('supervisor', 'Supervisor'), ('tecnico', 'Técnico'), ('asistente', 'Asistente'), ('auxiliar', 'Auxiliar'), ('conserje', 'Conserje'), ('otro', 'Otro')], max_length=20),
        ),
        migrations.AlterField(
            model_name='empleados',
            name='sex',
            field=models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')], max_length=1),
        ),
    ]
