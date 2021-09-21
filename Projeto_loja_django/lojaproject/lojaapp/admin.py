from django.contrib import admin
from.models import *

admin.site.register([Clientes,Categoria,Produto,carrinho,CarroProduto,ordem_pedido])
# Register your models here.
