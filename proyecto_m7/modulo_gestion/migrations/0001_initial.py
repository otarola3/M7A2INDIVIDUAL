# Generated by Django 4.2.1 on 2023-05-25 01:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(verbose_name='Cantidad')),
                ('seller', models.CharField(max_length=50, verbose_name='Vendedor')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
            ],
            options={
                'verbose_name': 'Orden',
                'verbose_name_plural': 'Ordenes',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('description', models.TextField(verbose_name='Descripcion')),
                ('price', models.IntegerField(verbose_name='Precio')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='state',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=50, verbose_name='Estado')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
                ('id_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modulo_gestion.order')),
            ],
            options={
                'verbose_name': 'Estado de Orden',
                'verbose_name_plural': 'Estado de ordenes',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(verbose_name='Cantidad')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
                ('id_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modulo_gestion.order')),
                ('id_price', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detalle_precio', to='modulo_gestion.product')),
                ('id_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detalle_producto', to='modulo_gestion.product')),
            ],
            options={
                'verbose_name': 'Detalle de Orden',
                'verbose_name_plural': 'Detalles de Ordenes',
                'ordering': ['-created'],
            },
        ),
        migrations.AddField(
            model_name='order',
            name='id_product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modulo_gestion.product'),
        ),
        migrations.AddField(
            model_name='order',
            name='id_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
