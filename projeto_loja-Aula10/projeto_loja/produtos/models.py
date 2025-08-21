# produtos/models.py (aula 10)

from django.db import models

##
# Primeira versão do model adicionado na aula 10
##
class Produto(models.Model):
    nome = models.CharField(
        max_length=100
        )

    descricao = models.TextField(

    )

    preco = models.DecimalField(
        max_digits=10, 
        decimal_places=2
        )

    tipo = models.CharField(
        max_length=50,
        blank=True, #para o formulário
        null=True, #para o banco de dados (ambas são boleanas e não obrigatórias para o preenchimento no site)
        )

    fabricante = models.CharField(
        max_length=60,
        blank=True,
        null=True,
        )

    modelo = models.CharField(
        max_length=60,
        blank=True,
        null=True,
        )

    quantidade = models.PositiveIntegerField(
        blank=True,
        null=True,
        default=0
        )

    status = models.BooleanField(
        default=True,
        )

    imagem = models.ImageField(
        upload_to='produtos/',
         blank=True, 
         null=True
         ) # Campo para imagem

        # Campos de data para registro de criação e última atualização
    data_criacao = models.DateTimeField(
        auto_now_add=True
        )

    data_atualizacao = models.DateTimeField(
        auto_now=True
        )

    class Meta:
        # Define a ordem padrão dos produtos por nome
        ordering = ['nome']

    def __str__(self):
        return self.nome
