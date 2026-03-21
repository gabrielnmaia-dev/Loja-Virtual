from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Produto
# Create your views here.


class ProdutoListView(ListView):
    model = Produto
    template_name = 'produtos/lista.html'
    context_object_name = 'produtos'

class ProdutoCreateView(CreateView):
    model = Produto
    fields = ['nome','preco','categoria','descricao','imagem']
    template_name = 'produtos/form.html'
    success_url = reverse_lazy('lista_produtos')

class ProdutoUpdateView(UpdateView):
    model = Produto
    fields = ['nome','preco','categoria','descricao','imagem']
    template_name = 'produtos/form.html'
    success_url = reverse_lazy('lista_produtos')

class ProdutoDeleteView(DeleteView):
    model = Produto
    template_name = 'produtos/confirm_delete.html'
    success_url = reverse_lazy('lista_produtos')