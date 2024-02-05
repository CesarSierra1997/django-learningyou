# Generated by Django 4.2.2 on 2024-02-05 02:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cohorte',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('codigo', models.CharField(max_length=50, verbose_name='Codigo')),
                ('descripcion', models.CharField(max_length=300, verbose_name='Descripcion')),
                ('fecha_creacion', models.DateField(auto_now=True, verbose_name='fecha de creacion')),
                ('fecha_fin', models.DateField(blank=True, null=True, verbose_name='fecha de Finalizacion')),
            ],
            options={
                'verbose_name': 'Cohorte',
                'verbose_name_plural': 'Cohortes',
                'ordering': ['-nombre'],
            },
        ),
        migrations.CreateModel(
            name='Leccion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=50, verbose_name='titulo de la lección')),
                ('codigo', models.CharField(max_length=50, verbose_name='Codigo Leccion')),
                ('descripcion', models.CharField(max_length=300, verbose_name='Descripcion')),
                ('fecha_creacion', models.DateField(auto_now=True, verbose_name='fecha de creacion')),
                ('fecha_fin', models.DateField(blank=True, null=True, verbose_name='fecha de Finalizacion')),
                ('cohorte_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cohortes.cohorte')),
            ],
            options={
                'verbose_name': 'Leccion',
                'verbose_name_plural': 'Lecciones',
                'ordering': ['-titulo'],
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('datecompleted', models.DateTimeField(blank=True, null=True)),
                ('important', models.BooleanField(default=False)),
                ('leccion_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cohortes.leccion')),
            ],
        ),
    ]