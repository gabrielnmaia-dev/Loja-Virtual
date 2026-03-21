from django.urls import path
from .views import *

urlpatterns = [
    path('', ProdutoListView.as_view(), name='lista_produtos'),
    path('novo/', ProdutoCreateView.as_view(), name='criar_produto'),
    path('editar/<int:pk>/', ProdutoUpdateView.as_view(), name='editar_produto'),
    path('deletar/<int:pk>/', ProdutoDeleteView.as_view(), name='deletar_produto'),
]