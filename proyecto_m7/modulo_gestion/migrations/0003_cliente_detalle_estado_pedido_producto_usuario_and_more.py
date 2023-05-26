# Generated by Django 4.2.1 on 2023-05-25 23:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('modulo_gestion', '0002_alter_order_id_product_alter_order_id_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.CharField(max_length=50, verbose_name='Direccion')),
                ('telefono', models.IntegerField(verbose_name='Telefono')),
                ('creditos', models.IntegerField(verbose_name='Creditos')),
                ('email', models.EmailField(max_length=50, verbose_name='Email')),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
                'ordering': ['-direccion'],
            },
        ),
        migrations.CreateModel(
            name='Detalle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(verbose_name='Cantidad')),
                ('total_detalle', models.IntegerField(verbose_name='Total')),
            ],
            options={
                'verbose_name': 'Detalle',
                'verbose_name_plural': 'Detalles',
                'ordering': ['-cantidad'],
            },
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Estado',
                'verbose_name_plural': 'Estados',
                'ordering': ['-nombre'],
            },
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(verbose_name='Fecha')),
                ('total', models.IntegerField(verbose_name='Total')),
                ('id_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modulo_gestion.cliente', verbose_name='Cliente')),
                ('id_estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modulo_gestion.estado', verbose_name='Estado')),
            ],
            options={
                'verbose_name': 'Pedido',
                'verbose_name_plural': 'Pedidos',
                'ordering': ['-fecha'],
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('precio', models.IntegerField(verbose_name='Precio')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
                'ordering': ['-nombre'],
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=50, verbose_name='Apellido')),
                ('email', models.EmailField(max_length=50, verbose_name='Email')),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
                'ordering': ['-nombre'],
            },
        ),
        migrations.RemoveField(
            model_name='orderdetail',
            name='id_order',
        ),
        migrations.RemoveField(
            model_name='orderdetail',
            name='id_price',
        ),
        migrations.RemoveField(
            model_name='orderdetail',
            name='id_product',
        ),
        migrations.RemoveField(
            model_name='state',
            name='id_order',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='OrderDetail',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='state',
        ),
        migrations.AddField(
            model_name='detalle',
            name='id_pedido',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modulo_gestion.pedido', verbose_name='Pedido'),
        ),
        migrations.AddField(
            model_name='detalle',
            name='id_producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modulo_gestion.producto', verbose_name='Producto'),
        ),
    ]
