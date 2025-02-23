from django.views.generic import TemplateView
import requests
from django.db.models import Count, Sum
from django.views.generic import ListView
from api.models import Categoria, Departamento, Fornecedor, Movimentacao



class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        # Substitua a requisição externa por um acesso interno à API
        url = '/api/bens/'  # Utilize a URL interna da sua API
        response = self.get_api_data(url)

        if response.status_code == 200:
            bens_data = response.json()
        else:
            bens_data = []

        context = super().get_context_data(**kwargs)
        context['bens'] = bens_data
        return context

    def get_api_data(self, url):
        # Método auxiliar para chamar a API interna
        request = self.request
        response = requests.get(f'http://127.0.0.1:8000{url}', cookies=request.COOKIES)
        return response

class CategoriaListView(ListView):
    template_name = 'categoria/lista_categorias.html'
    context_object_name = 'categorias'

    def get_queryset(self):
        
        return Categoria.objects.annotate(
            qtd_bens=Count('bem'),  
            valor_total=Sum('bem__valor_aquisicao') 
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        
        url = 'http://127.0.0.1:8000/api/categorias/'
        response = requests.get(url)

        
        if response.status_code == 200:
            categorias_api = response.json() 
            context['categorias_api'] = categorias_api  

        return context
    
class DepartamentoListView(ListView):
    template_name = 'departamento/lista_departamentos.html'
    context_object_name = 'departamentos'

    def get_queryset(self):
        
        return Departamento.objects.annotate(
            qtd_bens=Count('bem'), 
            valor_total=Sum('bem__valor_aquisicao')  
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

       
        url = 'http://127.0.0.1:8000/api/departamentos/'
        response = requests.get(url)

        
        if response.status_code == 200:
            departamentos_api = response.json()  
            context['departamentos_api'] = departamentos_api  

        return context

class FornecedorListView(ListView):
    template_name = 'fornecedor/lista_fornecedores.html'
    context_object_name = 'fornecedores'

    def get_queryset(self):
        
        return Fornecedor.objects.annotate(
            qtd_bens=Count('bem'),  
            valor_total=Sum('bem__valor_aquisicao')  
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        
        url = 'http://127.0.0.1:8000/api/fornecedores/'
        response = requests.get(url)

        
        if response.status_code == 200:
            fornecedores_api = response.json()  
            context['fornecedores_api'] = fornecedores_api  

        return context
    
class MovimentacaoListView(ListView):
    template_name = 'movimentacao/lista_movimentacoes.html'
    context_object_name = 'movimentacoes'

    def get_queryset(self):
        
        return Movimentacao.objects.annotate(
            qtd_bens=Count('bem'),  
            valor_total=Sum('bem__valor_aquisicao')  
        )
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        
        url = 'http://127.0.0.1:8000/api/movimentacaos/'
        response = requests.get(url)

        
        if response.status_code == 200:
            movimentacoes_api = response.json() 
            context['movimentacaos_api'] = movimentacoes_api  

        return context


