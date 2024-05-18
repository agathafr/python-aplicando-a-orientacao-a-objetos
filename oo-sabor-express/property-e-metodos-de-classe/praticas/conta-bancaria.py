''' Desafios:

- Crie uma classe chamada ContaBancaria com um construtor que aceita os parâmetros titular e saldo. Inicie o atributo ativo como False por padrão.

- Na classe ContaBancaria, adicione um método especial __str__ que retorna uma mensagem formatada com o titular e o saldo da conta. Crie duas instâncias da classe e imprima essas instâncias.

- Adicione um método de classe chamado ativar_conta à classe ContaBancaria que define o atributo ativo como True. Crie uma instância da classe, chame o método de classe e imprima o valor de ativo.

- Refatore a classe ContaBancaria para utilizar a abordagem "pythonica" na criação de atributos. Utilize propriedades, se necessário.

- Crie uma instância da classe e imprima o valor da propriedade titular.

'''

class ContaBancaria:
    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False

    @property
    def titular(self):
        return self._titular
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def ativo(self):
        return self._ativo

    def __str__(self):
        return print(f'{self.titular}, seu saldo é R$ {self.saldo}')
    
    @classmethod
    def ativar_conta(cls, conta):
        conta._ativo = True

conta_01 = ContaBancaria('Euclides', 1000)

ContaBancaria.ativar_conta(conta_01)

print(conta_01._ativo)
print(conta_01._titular)
