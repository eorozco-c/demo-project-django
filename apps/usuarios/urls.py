from django.urls import path
from . import views

app_name = "usuarios"

urlpatterns = [
    path('',views.index, name='index'),
    #path('usuarios/', views.usuarios, name='usuarios'),
    path('usuarios/', views.UsuarioListView.as_view(), name='usuarios'),
    # path('usuarios/nuevo/', views.nuevo, name='nuevo'),
    path('usuarios/nuevo/', views.UsuarioCreateView.as_view(), name='nuevo'),
    # path('usuarios/detalles/<int:id>', views.detalles, name='detalles'),
    path('usuarios/detalles/<int:pk>', views.UsuarioDetailView.as_view(), name='detalles'),
    # path('usuarios/editar/<int:id>', views.editar, name='editar'),
    path('usuarios/editar/<int:pk>', views.UsuarioUpdateView.as_view(), name='editar'),
    # path('usuarios/eliminar/<int:id>', views.eliminar, name='eliminar'),
    path('usuarios/eliminar/<int:pk>', views.UsuarioDeleteView.as_view(), name='eliminar'),
]
