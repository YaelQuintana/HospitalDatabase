# Generated by Django 4.2.7 on 2023-11-13 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipo_Med',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('descripcion', models.TextField()),
                ('units', models.IntegerField()),
                ('Last_Maint', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Medicamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('descripcion', models.TextField()),
                ('units', models.IntegerField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('LOTE', models.CharField(max_length=20)),
                ('expira', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Suministro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('descripcion', models.TextField()),
                ('units', models.IntegerField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('LOTE', models.CharField(max_length=20)),
                ('expira', models.DateField()),
                ('desechable', models.BooleanField(default=True)),
            ],
        ),
    ]
