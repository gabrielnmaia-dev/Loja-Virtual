from django.db import models

# Create your models here.
class Produto (models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    categoria = models.CharField(max_length=50)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='produtos/')

    def __str__(self):
        return self.nome