# Generated by Django 4.2.2 on 2023-07-22 13:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bodegas', '0006_detallemovimiento_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movimientobodega',
            name='bodega_origen',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bodegas.bodega'),
        ),
    ]
