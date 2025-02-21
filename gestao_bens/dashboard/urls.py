from django.urls import path
from .views import CategoriaListView, DepartamentoListView

urlpatterns = [
    path('categorias/', CategoriaListView.as_view(), name='lista_categorias'),  # Verifique se o nome da URL está correto
    path('departamentos/', DepartamentoListView.as_view(), name='lista_departamentos'),  # Verifique se o nome da URL está correto
    
]
