# Generated by Django 5.1.1 on 2024-09-09 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('correo', models.CharField(max_length=255)),
                ('telefono', models.CharField(max_length=15)),
                ('fecha_nacimiento', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
