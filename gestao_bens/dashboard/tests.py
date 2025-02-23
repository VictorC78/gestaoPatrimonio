from django.test import TestCase
from django.urls import reverse, resolve
from dashboard.views import CategoriaListView, DepartamentoListView, FornecedorListView, MovimentacaoListView

class URLTests(TestCase):

    def test_categoria_list_url_resolves(self):
        url = reverse('lista_categorias')
        self.assertEqual(resolve(url).func.view_class, CategoriaListView)

    def test_departamento_list_url_resolves(self):
        url = reverse('lista_departamentos')
        self.assertEqual(resolve(url).func.view_class, DepartamentoListView)

    def test_fornecedor_list_url_resolves(self):
        url = reverse('lista_fornecedores')
        self.assertEqual(resolve(url).func.view_class, FornecedorListView)

    def test_movimentacao_list_url_resolves(self):
        url = reverse('lista_movimentacoes')
        self.assertEqual(resolve(url).func.view_class, MovimentacaoListView)
