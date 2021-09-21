from django.urls import path
from django.urls import path
from.views import *
app_name = "lojaapp"
urlpatterns = [
    path("",HomeView.as_view(),name="home"),
    path("sobre/",SobreView.as_view(),name="sobre"), 
    path("contato/",ContatoView.as_view(),name="contato"), 
    path("todosprodutos/",TodosProdutosView.as_view(),name="TodosProdutos"), 
    path("produto/<slug:slug>/",ProdutosDetalheView.as_view(),name="produtodetalhe"), 
    path("addCarro-<int:prod_id>/",AddCarroView.as_view(),name="addCarro"),
    path("meu_carro/",MeuCarroView.as_view(),name="meucarro"),
    path("mamipular-carro/ <int:cp_id>/",ManipularView.as_view(),name="manipularcarro"),

]