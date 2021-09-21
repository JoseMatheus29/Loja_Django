from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import SlugField

class Clientes(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    nome = models.CharField(max_length=200)
    endereço = models.CharField(max_length=200,null=True,blank=True)
    data_cadastro = models.DateField(auto_now_add=True) 
    def __str__(self):
        return self.nome

class Categoria(models.Model):
    titulo = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    def __str__(self):
        return self.titulo

class Produto(models.Model):
    titulo = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    Categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    image = models.ImageField(upload_to="produtos")
    preco_mercado = models.PositiveIntegerField()
    venda = models.PositiveIntegerField()
    descricao = models.TextField()
    garantia = models.CharField(max_length=300, null=True, blank=True)
    devolucao = models.CharField(max_length=300, null=True, blank=True)
    visualização = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.titulo

class carrinho(models.Model):
    cliente = models.ForeignKey(Clientes,on_delete=models.SET_NULL,null=True, blank=True)
    total = models.PositiveIntegerField(default=0)
    criado_em = models.DateField(auto_now_add=True)
    def __str__(self):
        return "Carro " + str(self.id)

class CarroProduto(models.Model):
    carro = models.ForeignKey(carrinho,on_delete=models.CASCADE)
    Produto = models.ForeignKey(Produto,on_delete=models.CASCADE)
    avaliacao = models.PositiveIntegerField()
    quantidade = models.PositiveIntegerField()
    subtotal = models.PositiveIntegerField()
    def __str__(self):
        return "Carro: " +str(self.carro.id) + " carrinhoproduto:" + str(self.id)

PEDIDO_STATUS = (
    ("Pedido Recebido","Pedido Recebido"),
    ("Pedido Processando","Pedido Processando"),
    ("Pedido caminho","Pedido caminho"),
    ("Pedido Completado","Pedido Completado"),
    ("Pedido Cancelado","Pedido Cancelado"),
)
class ordem_pedido(models.Model):
    carro = models.OneToOneField(carrinho,on_delete=models.CASCADE)
    ordenado = models.CharField(max_length=10)
    endereço_envio = models.CharField(max_length=200)
    telefone = models.CharField(max_length=10)
    email = models.EmailField(null=True,blank=True)
    endereço_saida = models.CharField(max_length=200)
    subtotal = models.PositiveIntegerField()
    desconto = models.PositiveIntegerField()
    total = models.PositiveIntegerField()
    status = models.CharField(max_length=50, choices=PEDIDO_STATUS)

    def __str__(self):
        return "ordem_pedido" + str(self.id)