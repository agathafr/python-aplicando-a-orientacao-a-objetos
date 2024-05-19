'''
Crie uma nova classe chamada Carro que herda da classe Veiculo.
No construtor da classe Carro, utilize o método super() para chamar o construtor da classe pai e atribua o atributo específico cor à classe filha.
'''

from veiculo import Veiculo
class Carro(Veiculo):
    def __init__(self, marca, modelo, portas, cor):
         super().__init__(marca, modelo)
         self.portas = portas
         self.cor = cor
         
    def __str__(self):
        status = "ligado" if self._ligado else "desligado"
        return f'{self.marca.ljust(20)} | {self.modelo.ljust(20)} | {str(self.portas).ljust(20)} | {status} | {self.cor}'
   
    def ligar(self):
        pass 
