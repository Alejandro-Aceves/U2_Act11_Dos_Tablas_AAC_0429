from django.urls import path
from . import views

app_name = 'app_instrumentos'

urlpatterns = [
    path('', views.listar_instrumentos, name='listar_instrumentos'),
    path('instrumento/<int:id_instrumento>/', views.detalle_instrumento, name='detalle_instrumento'),
    path('crear/', views.crear_instrumento, name='crear_instrumento'),
    path('editar/<int:id_instrumento>/', views.editar_instrumento, name='editar_instrumento'),
    path('borrar/<int:id_instrumento>/', views.borrar_instrumento, name='borrar_instrumento'),
]