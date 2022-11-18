from .models import Categoria, Documento, Inventario, Usuarios,Pedido
from rest_framework import viewsets,permissions
from .serializers import CategoriaSerializer, DocumentoSerializer, InventariosSerializer,UsuariosSerializer,PedidoSerializer;

class DocumentoViewSet(viewsets.ModelViewSet):
    queryset=Documento.objects.all()
    permission_classes= [permissions.AllowAny]
    serializer_class=DocumentoSerializer

class UsuariosViewSet(viewsets.ModelViewSet):
    queryset=Usuarios.objects.all()
    permission_classes= [permissions.AllowAny]
    serializer_class=UsuariosSerializer

class PedidoViewSet(viewsets.ModelViewSet):
    queryset=Pedido.objects.all()
    permission_classes= [permissions.AllowAny]
    serializer_class=PedidoSerializer

class InventarioViewSet(viewsets.ModelViewSet):
    queryset=Inventario.objects.all()
    permission_classes= [permissions.AllowAny]
    serializer_class=InventariosSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset=Categoria.objects.all()
    permission_classes= [permissions.AllowAny]
    serializer_class=CategoriaSerializer