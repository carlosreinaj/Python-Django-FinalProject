# Generated by Django 5.1.1 on 2024-09-15 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autos', '0004_rename_año_auto_ano'),
    ]

    operations = [
        migrations.AddField(
            model_name='auto',
            name='fecha_actualizacion',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='auto',
            name='precio',
            field=models.DecimalField(decimal_places=2, default=10, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='auto',
            name='stock',
            field=models.FloatField(default=200),
            preserve_default=False,
        ),
    ]
