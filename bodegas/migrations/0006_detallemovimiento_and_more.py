# Generated by Django 4.2.2 on 2023-07-22 13:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bodegas', '0005_alter_movimiento_por_bodega_destino_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetalleMovimiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='bodegaproducto',
            name='bodegaDestino',
        ),
        migrations.RemoveField(
            model_name='bodegaproducto',
            name='bodegaOrigen',
        ),
        migrations.AddField(
            model_name='bodegaproducto',
            name='bodega',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='bodegas.bodega'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bodegaproducto',
            name='cantidad',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='MovimientoBodega',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('bodega_destino', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movimientos_destino', to='bodegas.bodega')),
                ('bodega_origen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movimientos_origen', to='bodegas.bodega')),
                ('productos', models.ManyToManyField(through='bodegas.DetalleMovimiento', to='bodegas.bodegaproducto')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='detallemovimiento',
            name='bodega_producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bodegas.bodegaproducto'),
        ),
        migrations.AddField(
            model_name='detallemovimiento',
            name='movimiento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bodegas.movimientobodega'),
        ),
    ]
