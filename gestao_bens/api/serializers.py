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
    categoria = serializers.PrimaryKeyRelatedField(queryset=Categoria.objects.all())  # O campo para receber o ID da categoria
    fornecedor = serializers.PrimaryKeyRelatedField(queryset=Fornecedor.objects.all())  # O campo para receber o ID do fornecedor
    departamento = serializers.PrimaryKeyRelatedField(queryset=Departamento.objects.all())  # O campo para receber o ID do departamento
    
    # Campos adicionais para retornar os nomes
    categoria_nome = serializers.SerializerMethodField()
    fornecedor_nome = serializers.SerializerMethodField()
    departamento_nome = serializers.SerializerMethodField()

    class Meta:
        model = Bem
        fields = '__all__'

    def get_categoria_nome(self, obj):
        return obj.categoria.nome  # Retorna o nome da categoria associada ao bem

    def get_fornecedor_nome(self, obj):
        return obj.fornecedor.nome  # Retorna o nome do fornecedor associado ao bem

    def get_departamento_nome(self, obj):
        return obj.departamento.nome  # Retorna o nome do departamento associado ao bem



class MovimentacaoSerializer(serializers.ModelSerializer):
    # O campo 'origem' não aparece no formulário.
    destino = serializers.PrimaryKeyRelatedField(queryset=Departamento.objects.all())

    class Meta:
        model = Movimentacao
        fields = ['bem', 'tipo_movimentacao', 'destino', 'justificativa', 'data_movimentacao']
    
    def validate(self, data):
        # Se a movimentação for do tipo 'transferência', valida se o bem já não está no destino
        if data['tipo_movimentacao'] == 'transferencia':
            bem = data['bem']
            if bem.departamento == data['destino']:
                raise serializers.ValidationError("O bem já está no departamento de destino.")
        return data

    def create(self, validated_data):
        bem = validated_data['bem']
        tipo_movimentacao = validated_data['tipo_movimentacao']

        # Se a movimentação for uma transferência, altera o departamento do bem
        if tipo_movimentacao == 'transferencia':
            bem.departamento = validated_data['destino']
            bem.save()

        # Cria e retorna a movimentação
        movimentacao = Movimentacao.objects.create(**validated_data)
        return movimentacao
