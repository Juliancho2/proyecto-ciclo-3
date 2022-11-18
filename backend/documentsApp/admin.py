import imp
from django.contrib import admin
from .models import Usuarios,Pedido,Documento,Inventario,Categoria
# Register your models here.

admin.site.register(Usuarios)
admin.site.register(Pedido)
admin.site.register(Documento)
admin.site.register(Inventario)
admin.site.register(Categoria)

