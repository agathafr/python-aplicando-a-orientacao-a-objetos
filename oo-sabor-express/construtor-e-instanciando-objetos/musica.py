''' Refaça essa classe Musica utilizando uma forma mais concisa e expressiva, aproveitando a sintaxe simplificada do Python. '''
class Musica:
    musicas = []

    def __init__(self, nome, artista, duracao):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao
        Musica.musicas.append(self)

    def __str__(self):
        return self.nome, self.artista, self.duracao
    
    def listar_musicas():
        for musica in Musica.musicas:
            print(f'{musica.nome} | {musica.artista} | {musica.duracao}')


musica_01 = Musica('THE GREATEST', 'Billie Elish', 293)

Musica.listar_musicas()
