# Generated by Django 4.2.7 on 2023-11-13 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BDMedico', '0002_empleado_test'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='name',
            field=models.TextField(),
        ),
    ]
