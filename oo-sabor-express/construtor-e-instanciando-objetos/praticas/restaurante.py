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
