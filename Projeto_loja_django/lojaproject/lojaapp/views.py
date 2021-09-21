from django.shortcuts import render, redirect 
from django.views.generic import View,TemplateView
from.models import *
# Create your views here.

class HomeView(TemplateView):
    template_name = "home.html"
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['Produto_list'] = Produto.objects.all().order_by("-id")
        return context
class SobreView(TemplateView):
    template_name = "sobre.html"
class ContatoView(TemplateView):
    template_name = "contato.html"

class TodosProdutosView(TemplateView):
    template_name = "todosprodutos.html"
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['todoscategorias'] = Categoria.objects.all()
        return context

class ProdutosDetalheView(TemplateView):
    template_name = "produtodetalhe.html"
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        url_slug = self.kwargs['slug']
        produto = Produto.objects.get(slug = url_slug)
        produto.visualização+=1
        produto.save()
        context['produto'] = produto
        return context
class AddCarroView(TemplateView):
    template_name="addproduto.html"
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        produto_id = self.kwargs['prod_id']
        produto_obj = Produto.objects.get(id = produto_id)
        carro_id = self.request.session.get("Carro_id ",None)
        if carro_id:
            carro_obj = carrinho.objects.get(id = carro_id)
            produto_no_carro = carro_obj.carroproduto_set.filter(Produto = produto_obj)
            if produto_no_carro:
                carroproduto = produto_no_carro.last()
                carroproduto.quantidade  += 1
                carroproduto.subtotal = produto_obj.venda
                carroproduto.save()
                carro_obj.total+= produto_obj.venda
                carro_obj.save()
            else:
                carroproduto = CarroProduto.objects.create(
                    carro = carro_obj,
                    Produto = produto_obj,
                    avaliacao = produto_obj.venda,
                    quantidade = 1,
                    subtotal = produto_obj.venda
                ) 
                carro_obj.total += produto_obj.venda
                carro_obj.save()
        else:
            carro_obj = carrinho.objects.create(total=0)
            self.request.session["Carro_id "] = carro_obj.id
            carroproduto = CarroProduto.objects.create(
                    carro = carro_obj,
                    Produto = produto_obj,
                    avaliacao = produto_obj.venda,
                    quantidade = 1,
                    subtotal = produto_obj.venda) 
            carro_obj.total+= produto_obj.venda
            carro_obj.save()
        return context
class MeuCarroView(TemplateView):
    template_name = "meucarro.html"
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        carro_id = self.request.session.get("Carro_id ",None)
        if carro_id:
            carro = carrinho.objects.get(id = carro_id)
        else:
            carro = None
        context['carro'] = carro
        return context
class ManipularView(View):
    def get(self,request,*args,**kwargs):
        return redirect("lojaapp:meucarro")
    