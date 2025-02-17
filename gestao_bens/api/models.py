from django.db import models

# Create your models here.

class Fornecedor(models.Model):
    nome = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=18, unique=True)
    contato = models.CharField(max_length=20)
    endereco =  models.TextField()
    email = models.EmailField()
    cep = models.CharField(max_length=10)
    
    def __str__(self):
        return self.nome
    
class Categoria(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    
    def __str__(self):
        return self.nome
    
class Departamento(models.Model):
    nome = models.CharField(max_length=255)
    localizacao = models.TextField()
    
    def __str__(self):
        return self.nome

class Bem(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    numero_tombamento = models.CharField(max_length=50, unique=True)
    tagRFID = models.CharField(max_length=50, unique=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    data_aquisicao = models.DateField()
    valor_aquisicao = models.DecimalField(max_digits=10, decimal_places=2)
    estado_conservacao = models.CharField(max_length=50, choices=[
        ('novo', 'Novo'),
        ('usado', 'Usado'),
        ('danificado', 'Danificado'),
        ('inservivel', 'Inservível'),
    ])
    situacao = models.CharField(max_length=50, choices=[
        ('ativo', 'Ativo'),
        ('baixado', 'Baixado'),
        ('emprestado', 'Emprestado'),
    ])

    def __str__(self):
        return self.nome
    
    
class Movimentacao(models.Model):
    tipo_movimentacao = models.CharField(max_length=50, choices=[
        ('transferencia', 'Transferência'),
        ('baixa', 'Baixa'),
        ('manutencao', 'Manutenção'),
        ('emprestimo', 'Empréstimo'),
    ])
    data_movimentacao = models.DateTimeField(auto_now_add=True)
    origem = models.ForeignKey(Departamento, related_name='origem', on_delete=models.CASCADE, null=True, blank=True)
    destino = models.ForeignKey(Departamento, related_name='destino', on_delete=models.CASCADE, null=True, blank=True)
    justificativa = models.TextField()
    bem = models.ForeignKey('Bem', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.tipo_movimentacao} de {self.bem.nome} - {self.data_movimentacao}"