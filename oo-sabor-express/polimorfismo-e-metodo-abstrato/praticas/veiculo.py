'''
Crie uma classe chamada Veiculo com um método abstrato chamado ligar.
No mesmo arquivo, crie um construtor para a classe Veiculo que aceita os parâmetros marca e modelo.
'''

from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self._ligado = False
    
    def __str__(self):
        status = "ligado" if self._ligado else "desligado"
        return f'{self.marca.ljust(20)} | {self.modelo.ljust(20)} | {status}'
    
    @abstractmethod
    def ligar(self):
        pass
