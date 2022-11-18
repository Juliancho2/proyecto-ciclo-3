
from rest_framework import serializers
from .models import Categoria, Documento, Inventario,Usuarios,Pedido

class CategoriaSerializer(serializers.ModelSerializer):
  class Meta:
     model=Categoria
     fields=('id','descripcion')


class DocumentoSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model=Documento
        fields=('id','tipo_doc','titulo','nombre_autor','fk_categoria','precio','img_url')
    def to_representation(self, instance):
        return {
          'id':instance.id,
          'titulo':instance.titulo,
          'nombre_autor':instance.nombre_autor,
          'tipo_doc':instance.tipo_doc,
          'fk_categoria':instance.fk_categoria.id,
          'categoria':instance.fk_categoria.descripcion,
          'precio':instance.precio,
          'img_url':instance.img_url,
        }
        
       
class  UsuariosSerializer(serializers.ModelSerializer):
      class Meta:
        model=Usuarios
        fields=('id','nombre_cli','apelido_cli', 'correo','direccion','tipo_cli')
        

class  PedidoSerializer(serializers.ModelSerializer):
     
      class Meta:
        model=Pedido
        fields=('id','fk_clie','fk_doc','fecha_pedido', 'detalle_alquiler_venta')
      def to_representation(self, instance):
        return {
          'id':instance.id,
          'fk_clie':instance.fk_clie.id,
          'fk_doc':instance.fk_doc.id,
          'cliente':instance.fk_clie.correo,
          'direccion':instance.fk_clie.direccion,
          'titulo':instance.fk_doc.titulo,
          'tipo_doc':instance.fk_doc.tipo_doc,
          'fecha_pedido':instance.fecha_pedido,
          'precio':instance.fk_doc.precio,
          'detalle_alquiler_venta':instance.detalle_alquiler_venta,
          
        }
        
class  InventariosSerializer(serializers.ModelSerializer):
      class Meta:
        model=Inventario
        fields=('id','fk_id_doc','cantidad_disponible')

        def to_representation(self, instance):
         return {
          'id':instance.id,
          'fk_id_doc':instance.fk_id_doc.id,
          'titulo':instance.fk_id_doc.titulo,
          'cantidad_disponible':instance.fk_id_doc.cantidad_disponible,
        }