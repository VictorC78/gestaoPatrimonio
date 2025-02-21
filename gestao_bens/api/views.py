from rest_framework import generics
from .models import Bem, Categoria, Departamento, Fornecedor, Movimentacao
from .serializers import BemSerializer, CategoriaSerializer, DepartamentoSerializer, FornecedorSerializer, MovimentacaoSerializer

# Listar e Criar fornecedores
class FornecedorListCreateView(generics.ListCreateAPIView):
    queryset = Fornecedor.objects.all()
    serializer_class = FornecedorSerializer

# Detalhar, Atualizar e Deletar fornecedor 
class FornecedorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Fornecedor.objects.all()
    serializer_class = FornecedorSerializer
    
# Listar e Criar Categorias
class CategoriaListCreateView(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

# Detalhar, Atualizar e Deletar Categoria 
class CategoriaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    
# Listar e Criar departamentos
class DepartamentoListCreateView(generics.ListCreateAPIView):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer

# Detalhar, Atualizar e Deletar Departamento 
class DepartamentoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer
    
# Listar e Criar bens
class BemListCreateView(generics.ListCreateAPIView):
    queryset = Bem.objects.all()
    serializer_class = BemSerializer

# Detalhar, Atualizar e Deletar bem 
class BemRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bem.objects.all()
    serializer_class = BemSerializer
    

class MovimentacaoListCreateView(generics.ListCreateAPIView):
    queryset = Movimentacao.objects.all()
    serializer_class = MovimentacaoSerializer


# Detalhar, Atualizar e Deletar Movimentação 
class MovimentacaoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movimentacao.objects.all()
    serializer_class = MovimentacaoSerializer
