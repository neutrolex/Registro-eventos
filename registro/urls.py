from django.urls import path
from . import views

urlpatterns = [
    path('', views.evento_list, name='evento_list'),
    path('crear/', views.evento_create, name='evento_create'),
    path('editar/<int:id>/', views.evento_update, name='evento_update'),
    path('eliminar/<int:id>/', views.evento_delete, name='evento_delete'),
]
