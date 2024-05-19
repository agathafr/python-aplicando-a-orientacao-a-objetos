'''
- Crie um Arquivo Main (main.py): Crie um arquivo chamado main.py no mesmo diretório que suas classes.
- Importe e Instancie Objetos: No arquivo main.py, importe as classes Carro e Moto. Em seguida, crie três instâncias de Carro e Moto com diferentes marcas, modelos, quantidade de portas e tipos.
- Exiba as Informações: Para cada instância, imprima no console as informações utilizando o método str.
'''

from carro import Carro
from moto import Moto

carro_01 = Carro('Toyota', 'Corolla', 4)
carro_02 = Carro('Honda', 'Civic', 4)
carro_03 = Carro('Ford', 'Mustang', 2)

moto_01 = Moto('Honda', 'CB 500X', 'Esportiva')
moto_02 = Moto('Yamaha', 'YZF-R3', 'Esportiva')
moto_03 = Moto('Honda', 'CB 300R', 'Casual')

print(carro_01)
print(carro_02)
print(carro_03)

print(moto_01)
print(moto_02)
print(moto_03)
