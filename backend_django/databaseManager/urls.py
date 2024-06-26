from django.urls import path
from .views import *


urlpatterns = [
    # Auth views
    path('auth/login/', LoginView.as_view(), name='auth_login'),
    path('auth/logout/', LogoutView.as_view(), name='auth_logout'),
    path('auth/signup/', SignupView.as_view(), name='auth_signup'),
    path('auth/register/', RegisterUserView.as_view(), name='register'),   
    path('crear-empleado/', CrearEmpleadoView.as_view(), name='crear-empleado'),
    path('listar-empleados/', ListarEmpleadosView.as_view(), name='listar-empleados'),
    path('modificar-empleado/<int:legajo>/', ModificarEmpleadoView.as_view(), name='modificar-empleado'),
    path('eliminar-empleado/<int:legajo>/', EliminarEmpleadoView.as_view(), name='eliminar-empleado'),
    path('crear-recibo/', CrearReciboView.as_view(), name='crear-recibo'),
    path('listar-recibos/', ListarReciboView.as_view(), name='listar-recibos'),
    path('modificar-recibo/<int:id_recibo>/', ModificarReciboView.as_view(), name='modificar-recibo'),
    path('eliminar-recibo/<int:id_recibo>/', EliminarReciboView.as_view(), name='eliminar-recibo'),
    path('crear-reclamo/', CrearReclamoView.as_view(), name='crear-reclamo'),
    path('listar-reclamos/', ListarReclamoView.as_view(), name='listar-reclamos'),
    path('modificar-reclamo/<int:id_recla>/', ModificarReclamoView.as_view(), name='modificar-reclamo'),    
    path('eliminar-reclamo/<int:id_recla>/', EliminarReclamoView.as_view(), name='eliminar-reclamo'),   
    path('pedidos/', PedidoListCreateView.as_view(), name='pedido-list-create'),
    path('pedidos/<int:pk>/', PedidoRetrieveUpdateDestroyView.as_view(), name='pedido-detail'),
    path('servicios/', ServiciosListCreateView.as_view(), name='servicio-list-create'),
    path('servicios/<int:pk>/', ServiciosRetrieveUpdateDestroyView.as_view(), name='servicio-detail'),
    path('categorias/', CategoriaServiciosListCreateView.as_view(), name='categoria-list-create'),
    path('categorias/<int:pk>/', CategoriaServiciosRetrieveUpdateDestroyView.as_view(), name='categoria-detail'),
    path('obra-social/', ObraSocialListCreateView.as_view(), name='obra-social-list-create'),
    path('obra-social/<int:pk>/', ObraSocialRetrieveUpdateDestroyView.as_view(), name='obra-social-detail'),
    path('art/', ArtListCreateView.as_view(), name='art-list-create'),
    path('art/<int:pk>/', ArtRetrieveUpdateDestroyView.as_view(), name='art-detail'),
]
