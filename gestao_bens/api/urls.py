from django.urls import path
from .views import BemListCreateView, BemRetrieveUpdateDestroyView, CategoriaListCreateView, CategoriaRetrieveUpdateDestroyView, DepartamentoListCreateView, DepartamentoRetrieveUpdateDestroyView, FornecedorListCreateView, FornecedorRetrieveUpdateDestroyView, MovimentacaoListCreateView, MovimentacaoRetrieveUpdateDestroyView

urlpatterns = [
    path('fornecedores/', FornecedorListCreateView.as_view(), name='fornecedor-list-create'),
    path('fornecedores/<int:pk>/', FornecedorRetrieveUpdateDestroyView.as_view(), name='fornecedor-detail'),
    path('categorias/', CategoriaListCreateView.as_view(), name='categoria-list-create'),
    path('categorias/<int:pk>/', CategoriaRetrieveUpdateDestroyView.as_view(), name='categoria-detail'),
    path('departamentos/', DepartamentoListCreateView.as_view(), name='departamento-list-create'),
    path('departamentos/<int:pk>/', DepartamentoRetrieveUpdateDestroyView.as_view(), name='departamento-detail'),
    path('bens/', BemListCreateView.as_view(), name='bem-list-create'),
    path('bens/<int:pk>/', BemRetrieveUpdateDestroyView.as_view(), name='bem-detail'),
    path('movimentacoes/', MovimentacaoListCreateView.as_view(), name='movimentacao-list-create'),
    path('movimentacoes/<int:pk>/', MovimentacaoRetrieveUpdateDestroyView.as_view(), name='movimentacao-detail'),
]
