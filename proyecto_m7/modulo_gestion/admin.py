from django.contrib import admin
from .models import Usuario, Cliente, Estado, Pedido, Producto


# Register your models here.


##class ProductoAdmin(admin.ModelAdmin):
   #readonly_fields = ('created', 'updated')
    
admin.site.register(Usuario)
admin.site.register(Cliente)
admin.site.register(Estado)
admin.site.register(Pedido)
admin.site.register(Producto)