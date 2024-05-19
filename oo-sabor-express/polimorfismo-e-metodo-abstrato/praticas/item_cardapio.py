from abc import ABC, abstractmethod

class ItemCardapio(ABC) :
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco
        
    def __str__(self):
        return f'Nome do item: {self._nome.ljust(20)} | Preço do item: {str(self._preco).ljust(20)}'
    
    @abstractmethod
    def aplicar_desconto(self):
        pass
