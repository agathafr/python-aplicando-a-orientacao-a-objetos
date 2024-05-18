# Prática 01
''' Implemente uma classe chamada Carro com os atributos básicos, como modelo, cor e ano. Crie uma instância dessa classe e atribua valores aos seus atributos. '''

class Carro:
    carros = []

    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        Carro.carros.append(self)

    def __str__(self):
        return self.modelo, self.cor, self.ano
    
    def listar_carros():
        for carro in Carro.carros:
            print(f'{carro.modelo}, {carro.cor}, {carro.ano}')

carro_01 = Carro('Fiat', 'Azul Petróleo', '2004')
Carro.listar_carros()

# Prática 02
''' Crie uma classe chamada Restaurante com os atributos nome, categoria, ativo e crie mais 2 atributos. Instancie um restaurante e atribua valores aos seus atributos. '''

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria, prato_do_dia, frete):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        self.prato_do_dia = prato_do_dia
        self.frete = frete
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return self.nome, self.categoria, self.ativo, self.prato_do_dia, self.frete
    
    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome} | {restaurante.categoria} | {restaurante.ativo} | {restaurante.prato_do_dia} | {restaurante.frete}')
    
restaurante_01 = Restaurante('Doce demais', 'Sobremesa', 'Banana com Canela', 5.0)
Restaurante.listar_restaurantes()

