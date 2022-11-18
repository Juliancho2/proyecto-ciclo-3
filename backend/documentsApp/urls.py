from rest_framework import routers
from .api import DocumentoViewSet, InventarioViewSet,UsuariosViewSet,PedidoViewSet,CategoriaViewSet

router= routers.DefaultRouter()

router.register('api/productos',DocumentoViewSet,'documento')
router.register('api/usuarios',UsuariosViewSet,'usuarios')
router.register('api/pedido',PedidoViewSet,'pedido')
router.register('api/inventario',InventarioViewSet,'inventario')
router.register('api/categoria',CategoriaViewSet,'categoria')







urlpatterns=router.urls
