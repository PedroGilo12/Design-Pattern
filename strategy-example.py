from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

# Classe Auxiliar:
class Produto():

    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor
    

class DescontoStrategy(ABC): # Strategy

    @abstractmethod
    def desconto(self, valor):
        pass

class DescontoDiasUteisStrategy(DescontoStrategy):
    
    def desconto(self, valor):
        return valor*0.9
    
class DescontoFimDeSemanaStrategy(DescontoStrategy):

    def desconto(self, valor):
        return valor*0.75

class ShoppingCart(): # Contexto

    def __init__(self):
        self.produtos = []
        self.valor_produtos = []

    def add_produto(self, Produto):
        self.produtos.append(Produto.nome)
        self.valor_produtos.append(Produto.valor)

    def get_subtotal(self):
        return sum(self.valor_produtos)
    
    def get_totalComDesconto(self, strategy: DescontoStrategy):
        valor = sum(self.valor_produtos)
        self.total = strategy.desconto(self, valor)

        return self.total


carrinho1 = ShoppingCart()
carrinho1.add_produto(Produto("Batata", 15))
carrinho1.add_produto(Produto("Feijão", 12))
carrinho1.add_produto(Produto("Carne", 30))
carrinho1.add_produto(Produto("Arroz", 50))

print("Valor total da compra durante a semana: {}".format(carrinho1.get_totalComDesconto(DescontoDiasUteisStrategy)))
print("valor total da compra nos fins de semana: {}".format(carrinho1.get_totalComDesconto(DescontoFimDeSemanaStrategy)))
