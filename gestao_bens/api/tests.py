import random
import string
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Fornecedor, Categoria, Departamento, Bem, Movimentacao
from django.urls import reverse


def generate_unique_cnpj():
    # Função para gerar um CNPJ fictício único (simulando um CNPJ)
    return ''.join(random.choices(string.digits, k=18))  # Gerando um CNPJ de 18 dígitos

class FornecedorTests(APITestCase):
    def setUp(self):
        # Geração de CNPJ único para o fornecedor de teste
        self.fornecedor_data = {
            'nome': 'Fornecedor Teste',
            'cnpj': generate_unique_cnpj(),  # Gera um CNPJ único
            'contato': '123456789',
            'endereco': 'Rua Teste, 123',
            'email': 'fornecedor@teste.com',
            'cep': '12345-678',
        }
        # Criação do fornecedor utilizando dados de teste
        self.fornecedor = Fornecedor.objects.create(**self.fornecedor_data)

        # Garantindo que o CNPJ do próximo fornecedor será único
        self.fornecedor_data['cnpj'] = generate_unique_cnpj()

        self.url = reverse('fornecedor-list-create')  # URL para a criação de fornecedores

    def test_create_fornecedor(self):
        # Criação do fornecedor via POST
        response = self.client.post(self.url, self.fornecedor_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['nome'], self.fornecedor_data['nome'])
        self.assertEqual(response.data['cnpj'], self.fornecedor_data['cnpj'])
        self.assertEqual(response.data['email'], self.fornecedor_data['email'])

    def test_get_fornecedor_list(self):
        # Obtendo a lista de fornecedores via GET
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Deve retornar 1 fornecedor

    def test_get_fornecedor_detail(self):
        # Obtendo os detalhes de um fornecedor via GET
        url = reverse('fornecedor-detail', kwargs={'pk': self.fornecedor.pk})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nome'], self.fornecedor_data['nome'])

    def test_update_fornecedor(self):
        # Atualizando o fornecedor via PUT
        url = reverse('fornecedor-detail', kwargs={'pk': self.fornecedor.pk})
        updated_data = {'nome': 'Fornecedor Atualizado', 'cnpj': '12.345.678/0001-88', 'contato': '987654321', 'endereco': 'Rua Atualizada, 123', 'email': 'atualizado@teste.com', 'cep': '98765-432'}
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nome'], updated_data['nome'])

    def test_delete_fornecedor(self):
        # Deletando o fornecedor via DELETE
        url = reverse('fornecedor-detail', kwargs={'pk': self.fornecedor.pk})
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class CategoriaTests(APITestCase):
    
    def setUp(self):
        self.url = reverse('categoria-list-create')
        self.categoria_data = {'nome': 'Categoria 1', 'descricao': 'Descrição da Categoria'}
        self.categoria = Categoria.objects.create(**self.categoria_data)

    def test_create_categoria(self):
        response = self.client.post(self.url, self.categoria_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_categoria_list(self):
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_categoria_detail(self):
        url = reverse('categoria-detail', kwargs={'pk': self.categoria.pk})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nome'], self.categoria.nome)

    def test_update_categoria(self):
        url = reverse('categoria-detail', kwargs={'pk': self.categoria.pk})
        updated_data = {'nome': 'Categoria Atualizada'}
        response = self.client.patch(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nome'], updated_data['nome'])

    def test_delete_categoria(self):
        url = reverse('categoria-detail', kwargs={'pk': self.categoria.pk})
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class DepartamentoTests(APITestCase):

    def setUp(self):
        self.url = reverse('departamento-list-create')
        self.departamento_data = {'nome': 'Departamento 1', 'localizacao': 'Local 1'}
        self.departamento = Departamento.objects.create(**self.departamento_data)

    def test_create_departamento(self):
        response = self.client.post(self.url, self.departamento_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_departamento_list(self):
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_departamento_detail(self):
        url = reverse('departamento-detail', kwargs={'pk': self.departamento.pk})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nome'], self.departamento.nome)

    def test_update_departamento(self):
        url = reverse('departamento-detail', kwargs={'pk': self.departamento.pk})
        updated_data = {'nome': 'Departamento Atualizado'}
        response = self.client.patch(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nome'], updated_data['nome'])

    def test_delete_departamento(self):
        url = reverse('departamento-detail', kwargs={'pk': self.departamento.pk})
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class BemTests(APITestCase):
    def setUp(self):
        # Criando as dependências necessárias antes dos testes
        self.categoria = Categoria.objects.create(nome='Categoria 1')
        self.fornecedor = Fornecedor.objects.create(nome='Fornecedor 1')
        self.departamento_origem = Departamento.objects.create(nome='Departamento 1')

        self.bem_data = {
            'nome': 'Bem A',
            'descricao': 'Descrição do Bem',
            'numero_tombamento': '1234567890',
            'tagRFID': '123456',
            'categoria': self.categoria.id,  # Passando o ID da Categoria
            'fornecedor': self.fornecedor.id,  # Passando o ID do Fornecedor
            'departamento': self.departamento_origem.id,  # Passando o ID do Departamento
            'data_aquisicao': '2025-01-01',
            'valor_aquisicao': 100.00,
            'estado_conservacao': 'novo',
            'situacao': 'ativo',
            'qnt': 1
        }

    def test_create_bem(self):
        # Teste para criar um novo Bem
        response = self.client.post('/api/bens/', self.bem_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Bem.objects.count(), 1)

    def test_delete_bem(self):
        # Teste para deletar um Bem
        bem = Bem.objects.create(**self.bem_data)
        response = self.client.delete(f'/api/bens/{bem.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Bem.objects.count(), 0)

    def test_get_bem_detail(self):
        # Teste para obter detalhes de um Bem
        bem = Bem.objects.create(**self.bem_data)
        response = self.client.get(f'/api/bens/{bem.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nome'], 'Bem A')

    def test_get_bem_list(self):
        # Teste para listar todos os Bens
        Bem.objects.create(**self.bem_data)
        response = self.client.get('/api/bens/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_update_bem(self):
        # Atualizar o bem com dados válidos
        updated_bem_data = {
            'nome': 'Bem Atualizado',
            'descricao': 'Descrição atualizada',
            'categoria': self.categoria.pk,  
            'valor': 1500,
        }
        response = self.client.put(reverse('bem-detail', kwargs={'pk': self.bem.id}), updated_bem_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nome'], updated_bem_data['nome'])
        self.assertEqual(response.data['descricao'], updated_bem_data['descricao'])



class MovimentacaoTests(APITestCase):
    def setUp(self):
        # Criando as dependências necessárias antes dos testes
        self.categoria = Categoria.objects.create(nome='Categoria 1')
        self.fornecedor = Fornecedor.objects.create(nome='Fornecedor 1')
        self.departamento_origem = Departamento.objects.create(nome='Departamento 1')

        self.bem_data = {
            'nome': 'Bem A',
            'descricao': 'Descrição do Bem',
            'numero_tombamento': '1234567890',
            'tagRFID': '123456',
            'categoria': 1,  # Atribuindo uma instância de Categoria
            'fornecedor': 1,  # Atribuindo uma instância de Fornecedor
            'departamento': 1,  # Atribuindo uma instância de Departamento
            'data_aquisicao': '2025-01-01',
            'valor_aquisicao': 100.00,
            'estado_conservacao': 'novo',
            'situacao': 'ativo',
            'qnt': 1
        }

    def test_create_movimentacao(self):
        # Teste para criar uma movimentação
        response = self.client.post('/api/movimentacoes/', self.bem_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    

    def test_get_movimentacao_detail(self):
        # Teste para obter detalhes de uma movimentação
        bem = Bem.objects.create(**self.bem_data)
        response = self.client.get(f'/api/movimentacoes/{bem.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_movimentacao_list(self):
        # Teste para listar todas as movimentações
        Bem.objects.create(**self.bem_data)
        response = self.client.get('/api/movimentacoes/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)




