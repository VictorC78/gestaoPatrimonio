from rest_framework import serializers
from .models import Bem, Categoria, Departamento, Fornecedor, Movimentacao

class FornecedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fornecedor
        fields = '__all__'  
        
class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'  
        
class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = '__all__'  
        
class BemSerializer(serializers.ModelSerializer):
    categoria = serializers.StringRelatedField()
    fornecedor = serializers.StringRelatedField()
    departamento = serializers.StringRelatedField()

    class Meta:
        model = Bem
        fields = '__all__'
        
class MovimentacaoSerializer(serializers.ModelSerializer):
    bem = serializers.StringRelatedField()
    origem = serializers.StringRelatedField()
    destino = serializers.StringRelatedField()
    responsavel = serializers.StringRelatedField()

    class Meta:
        model = Movimentacao
        fields = '__all__'  # Inclui todos os campos do modelo

