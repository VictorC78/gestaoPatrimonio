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
    categoria = serializers.PrimaryKeyRelatedField(queryset=Categoria.objects.all()) 
    fornecedor = serializers.PrimaryKeyRelatedField(queryset=Fornecedor.objects.all())  
    departamento = serializers.PrimaryKeyRelatedField(queryset=Departamento.objects.all())  
    
    
    categoria_nome = serializers.SerializerMethodField()
    fornecedor_nome = serializers.SerializerMethodField()
    departamento_nome = serializers.SerializerMethodField()

    class Meta:
        model = Bem
        fields = '__all__'

    def get_categoria_nome(self, obj):
        return obj.categoria.nome  

    def get_fornecedor_nome(self, obj):
        return obj.fornecedor.nome  

    def get_departamento_nome(self, obj):
        return obj.departamento.nome 



class MovimentacaoSerializer(serializers.ModelSerializer):
    
    destino = serializers.PrimaryKeyRelatedField(queryset=Departamento.objects.all())

    class Meta:
        model = Movimentacao
        fields = ['bem', 'tipo_movimentacao', 'destino', 'justificativa', 'data_movimentacao']
    
    def validate(self, data):
       
        if data['tipo_movimentacao'] == 'transferencia':
            bem = data['bem']
            if bem.departamento == data['destino']:
                raise serializers.ValidationError("O bem já está no departamento de destino.")
        return data

    def create(self, validated_data):
        bem = validated_data['bem']
        tipo_movimentacao = validated_data['tipo_movimentacao']

        if tipo_movimentacao == 'transferencia':
            bem.departamento = validated_data['destino']
            bem.save()

        
        movimentacao = Movimentacao.objects.create(**validated_data)
        return movimentacao
