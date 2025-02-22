from django.urls import path
from .views import CategoriaListView, DepartamentoListView, FornecedorListView, MovimentacaoListView

urlpatterns = [
    path('categorias/', CategoriaListView.as_view(), name='lista_categorias'),  
    path('departamentos/', DepartamentoListView.as_view(), name='lista_departamentos'), 
    path('fornecedores/', FornecedorListView.as_view(), name='lista_fornecedores'),  
    path('movimentacoes/', MovimentacaoListView.as_view(), name='lista_movimentacoes'),  
    
    
    
]
