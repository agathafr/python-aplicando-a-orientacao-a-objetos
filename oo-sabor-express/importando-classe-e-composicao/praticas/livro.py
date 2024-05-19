'''
- Crie uma classe chamada Livro com um construtor que aceita os parâmetros titulo, autor e ano_publicacao. Inicie um atributo chamado disponivel como True por padrão.

- Na classe Livro, adicione um método especial str que retorna uma mensagem formatada com o título, autor e ano de publicação do livro. Crie duas instâncias da classe Livro e imprima essas instâncias.

- Adicione um método de instância chamado emprestar à classe Livro que define o atributo disponivel como False. Crie uma instância da classe, chame o método emprestar e imprima se o livro está disponível ou não.

- Adicione um método estático chamado verificar_disponibilidade à classe Livro que recebe um ano como parâmetro e retorna uma lista dos livros disponíveis publicados nesse ano.

'''
class Livro:
    livros = []

    def __init__(self, titulo, autor, ano_publicacao):
        self._titulo = titulo
        self._autor = autor
        self._ano_publicacao = ano_publicacao
        self._disponivel = True
        Livro.livros.append(self)

    def __str__(self):
        return f'O livro {self._titulo} do autor {self._autor} foi publicado no ano {self._ano_publicacao}'
    
    def listar_livros():
        for livro in Livro.livros:
            print(f'{livro._titulo.ljust(35)} | {livro._autor.ljust(35)} | {str(livro._ano_publicacao).ljust(30)} | {livro._disponivel}')

    def emprestar(self):
        self._disponivel = False

    @staticmethod
    def verificar_disponibilidade(ano):
        livros_disponiveis = [livro for livro in Livro.livros if livro._ano_publicacao == ano]
        if livros_disponiveis:
            for livro in livros_disponiveis:
                    print(f'{livro._titulo} é um livro disponível publicado no ano {livro._ano_publicacao}')
        else:
            print(f'Não há livros disponíveis que foram publicados em {ano}')

livro_01 = Livro('O Mundo de Sofia', 'Jostein Gaarder', 1991)
livro_02 = Livro('A menina que roubava livros', 'Markus Zusak', 2005)


print(livro_01)
