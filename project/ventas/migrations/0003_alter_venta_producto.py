# Generated by Django 5.1.1 on 2024-09-18 23:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autos', '0006_auto_imagen_auto_autos_auto_modelo_1a394e_idx_and_more'),
        ('ventas', '0002_alter_venta_cantidad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autos.auto'),
        ),
    ]
