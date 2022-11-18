from email.policy import default
from venv import create
from django.db import models

# Create your models here.
class Usuarios(models.Model):
    nombre_cli= models.CharField(max_length=100)
    apelido_cli= models.CharField(max_length=100)
    correo = models.EmailField(unique=True,max_length=70,null=True)
    direccion=models.CharField(max_length=100)
    contraseña=models.CharField(max_length=100)
    tipo_cli=models.BooleanField(default=False)
    estado_cli=models.BooleanField(default=False)
    
    def __str__(self):
        return self.nombre_cli +' ' +self.apelido_cli

class Categoria(models.Model):
    descripcion=models.CharField(max_length=200)
    def __str__(self):
        return self.descripcion

class Documento(models.Model):
    tipo_doc=models.CharField(max_length=100, )
    titulo=models.CharField(max_length=100 )
    nombre_autor=models.CharField(max_length=100)
    fk_categoria=models.ForeignKey(Categoria,on_delete=models.CASCADE)
    precio=models.FloatField(verbose_name='$',blank=True, null=True, )
    img_url=models.CharField(max_length=200)
    
    def __str__(self):
        return self.titulo 


class Pedido(models.Model):
    fk_clie=models.ForeignKey(Usuarios,on_delete=models.CASCADE)
    fk_doc=models.ForeignKey(Documento,on_delete=models.CASCADE)
    fecha_pedido=models.DateTimeField(auto_now_add=True)
    detalle_alquiler_venta=models.CharField(max_length=100)
    
    def __str__(self):
        return self.fecha_pedido 


class Inventario(models.Model):
    fk_id_doc=models.ForeignKey(Documento,on_delete=models.CASCADE)
    cantidad_disponible=models.FloatField(blank=True, null=True, )
    
    def __str__(self):
        return str(int(self.cantidad_disponible))


