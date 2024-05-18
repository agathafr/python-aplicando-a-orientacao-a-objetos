class Restaurante:
    nome = ''
    categoria = ''
    ativo = False

restaurante_praca = Restaurante()

# Prática 01
''' Atribua o valor 'Italiana' ao atributo categoria da instância restaurante_praca da classe Restaurante '''

restaurante_praca.categoria = 'Italiana'

# Prática 02
''' Acesse o valor do atributo nome da instância restaurante_praca da classe Restaurante. '''

nome_do_restaurante = restaurante_praca.nome

# Prática 03
''' Verifique o valor inicial do atributo ativo para a instância restaurante_praca e exiba uma mensagem informando se o restaurante está ativo ou inativo. '''

print('O restaurante está ativo!' if restaurante_praca.ativo else 'O restaurante está inativo!')

# Prática 04
''' Acesse o valor do atributo de classe categoria diretamente da classe Restaurante e armazene em uma variável chamada categoria. '''

categoria = Restaurante.categoria

# Prática 05
''' Altere o valor do atributo nome para 'Bistrô'. '''

restaurante_praca.nome = 'Bistrô'

# Prática 06
''' Crie uma nova instância da classe Restaurante chamada restaurante_pizza com o nome 'Pizza Place' e categoria 'Fast Food'. '''

restaurante_pizza = Restaurante()

restaurante_pizza.nome = 'Pizza Place'

restaurante_pizza.categoria = 'Fast Food'

# Prática 07
''' Verifique se a categoria da instância restaurante_pizza é 'Fast Food' '''
print('A categoria da instância restaurante_pizza é Fast Food.' if restaurante_pizza.categoria == 'Fast Food' else f'A categoria da instância restaurante_pizza é {restaurante_pizza.categoria}')

# Prática 08
''' Mude o estado da instância restaurante_pizza para ativo. '''
restaurante_pizza.ativo = True

# Prática 09 
''' Imprima no console o nome e a categoria da instância restaurante_praca. '''
print(f'O nome da instância restaurante_praca é {restaurante_praca.nome} e a categoria dele é {restaurante_praca.categoria}.')
