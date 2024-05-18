''' Crie uma classe chamada Musica com os seguintes atributos e crie 3 objetos definindo cada atributo. '''
class Musica:
    nome = ''
    artista = '' 
    duracao = 0

pop = Musica()
pop.nome = 'Lovely'
pop.artista = 'Billie Elish'
pop.duracao = 200

print(f'Música: {pop.nome}  - Banda: {pop.artista} - {pop.duracao} segundos')
