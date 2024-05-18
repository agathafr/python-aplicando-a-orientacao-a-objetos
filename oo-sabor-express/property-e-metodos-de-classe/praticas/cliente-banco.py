''' 
- Crie uma classe chamada ClienteBanco com um construtor que aceita 5 atributos. Instancie 3 objetos desta classe e atribua valores aos seus atributos através do método construtor.
- Crie um método de classe para a conta ClienteBanco.

'''
class ClienteBanco:
    clientes = []

    def __init__(self, nome, idade, endereco, telefone, email):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
        self.telefone = telefone
        self.email = email
        ClienteBanco.clientes.append(self)

    @classmethod
    def listar_clientes(cls):
        return [cliente.nome for cliente in cls.clientes]

cliente_01 = ClienteBanco('Elias', 30, 'Rua A, 123', '1234-5678', 'elias@email.com')
cliente_02 = ClienteBanco('Fernanda', 25, 'Rua B, 456', '2345-6789', 'fernanda@email.com')
cliente_03 = ClienteBanco('Gabriel', 40, 'Rua C, 789', '3456-7890', 'gabriel@email.com')

print(ClienteBanco.listar_clientes())
