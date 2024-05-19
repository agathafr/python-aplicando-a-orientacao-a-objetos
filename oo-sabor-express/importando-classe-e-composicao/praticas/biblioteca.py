'''
- Crie um arquivo chamado biblioteca.py e importe a classe Livro neste arquivo.

- No arquivo biblioteca.py, empreste o livro chamando o método emprestar e imprima se o livro está disponível ou não após o empréstimo.

- No arquivo biblioteca.py, utilize o método estático verificar_disponibilidade para obter a lista de livros disponíveis publicados em um ano específico.

'''

from livro import Livro

livro_01 = Livro('A vida dos estoicos', 'Stephen Hanselman e Ryan Holiday', 2021)
 
Livro.emprestar(livro_01)
Livro.verificar_disponibilidade(2021)
Livro.listar_livros()
print(livro_01)
