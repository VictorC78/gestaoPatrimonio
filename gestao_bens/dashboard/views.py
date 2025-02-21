from django.views.generic import TemplateView
import requests
from django.db.models import Count, Sum
from django.views.generic import ListView
from api.models import Categoria, Departamento


class IndexView(TemplateView): 

    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        
        url = 'http://127.0.0.1:8000/api/bens/'  
        response = requests.get(url)
        
        
        if response.status_code == 200:
            bens_data = response.json()  
        else:
            bens_data = [] 
        
        context = super().get_context_data(**kwargs)
        context['bens'] = bens_data  
        return context

class CategoriaListView(ListView):
    template_name = 'categoria/lista_categorias.html'
    context_object_name = 'categorias'

    def get_queryset(self):
        # Obtém todas as categorias e anota a quantidade de bens e o valor total
        return Categoria.objects.annotate(
            qtd_bens=Count('bem'),  # Conta a quantidade de bens na categoria
            valor_total=Sum('bem__valor_aquisicao')  # Soma o valor dos bens na categoria
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Aqui, fazemos uma requisição à API se necessário (opcional)
        url = 'http://127.0.0.1:8000/api/categorias/'
        response = requests.get(url)

        # Adiciona as categorias da API ao contexto, caso a resposta seja bem-sucedida
        if response.status_code == 200:
            categorias_api = response.json()  # Extrai os dados da API
            context['categorias_api'] = categorias_api  # Adiciona ao contexto para exibição

        return context
    
class DepartamentoListView(ListView):
    template_name = 'departamento/lista_departamentos.html'
    context_object_name = 'departamentos'

    def get_queryset(self):
        # Obtém todas as departamentos e anota a quantidade de bens e o valor total
        return Departamento.objects.annotate(
            qtd_bens=Count('bem'),  # Conta a quantidade de bens na departamento
            valor_total=Sum('bem__valor_aquisicao')  # Soma o valor dos bens na departamento
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Aqui, fazemos uma requisição à API se necessário (opcional)
        url = 'http://127.0.0.1:8000/api/departamentos/'
        response = requests.get(url)

        # Adiciona as departamentos da API ao contexto, caso a resposta seja bem-sucedida
        if response.status_code == 200:
            departamentos_api = response.json()  # Extrai os dados da API
            context['departamentos_api'] = departamentos_api  # Adiciona ao contexto para exibição

        return context

