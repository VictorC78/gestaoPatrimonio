from django.views.generic import TemplateView
import requests

class IndexView(TemplateView):
    template_name = 'index.html' 

    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        # URL da sua API 'Bens'
        url = 'http://127.0.0.1:8000/api/bens/'  
        response = requests.get(url)
        
        # Checando se a requisição foi bem-sucedida
        if response.status_code == 200:
            bens_data = response.json()  # Pegando os dados da API como um dicionário JSON
        else:
            bens_data = []  # Se a requisição falhar, passando uma lista vazia
        
        context = super().get_context_data(**kwargs)
        context['bens'] = bens_data  # Passando os dados para o template
        return context