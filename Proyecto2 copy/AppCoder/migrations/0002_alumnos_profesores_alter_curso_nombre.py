# Generated by Django 5.0.3 on 2024-04-10 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ALumnos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_alumno', models.CharField(max_length=20)),
                ('apellido_alumno', models.CharField(max_length=20)),
                ('edad_alumno', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Profesores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_prof', models.CharField(max_length=20)),
                ('apellido_prof', models.CharField(max_length=29)),
                ('curso_prfo', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='curso',
            name='nombre',
            field=models.CharField(max_length=30),
        ),
    ]