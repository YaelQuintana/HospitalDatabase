# Generated by Django 4.2.7 on 2023-11-13 08:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BDMedico', '0003_alter_test_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='equipo_med',
            old_name='descripcion',
            new_name='description',
        ),
    ]
