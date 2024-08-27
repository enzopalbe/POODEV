
class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao

    def __str__(self):
        return f"'{self.titulo}' por {self.autor} ({self.ano_publicacao})"




class Biblioteca:
    def __init__(self):
        self.livros = []  # Lista para armazenar objetos da classe Livro

    def adicionar_livro(self, livro):
        if isinstance(livro, Livro):
            self.livros.append(livro)
            print(f"Livro '{livro.titulo}' adicionado à biblioteca.")
        else:
            print("Erro: O objeto adicionado não é um Livro.")

    def remover_livro(self, titulo):
        livro_para_remover = None
        for livro in self.livros:
            if livro.titulo == titulo:
                livro_para_remover = livro
                break

        if livro_para_remover:
            self.livros.remove(livro_para_remover)
            print(f"Livro '{titulo}' removido da biblioteca.")
        else:
            print(f"Livro '{titulo}' não encontrado na biblioteca.")

    def listar_livros(self):
        if not self.livros:
            print("A biblioteca está vazia.")
        else:
            print("Livros na biblioteca:")
            for livro in self.livros:
                print(livro)

    # Método para criar um iterador
    def __iter__(self):
        self._iter_index = 0  # Inicializa o índice do iterador
        return self

    # Método __next__ para implementar o protocolo de iterador
    def __next__(self):
        if self._iter_index < len(self.livros):
            livro = self.livros[self._iter_index]
            self._iter_index += 1
            return livro
        else:
            raise StopIteration  # Exceção para indicar o fim da iteração


# Exemplo de uso
livro1 = Livro("1984", "George Orwell", 1949)
livro2 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", 1954)
livro3 = Livro("A Revolução dos Bichos", "George Orwell", 1945)

biblioteca = Biblioteca()
biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)
biblioteca.adicionar_livro(livro3)

print("Listando livros com iteração:")
for livro in biblioteca:
    print(livro)  # Itera sobre os livros usando o iterador

# Removendo um livro e listando novamente
biblioteca.remover_livro("1984")
print("Listando livros após remoção:")
for livro in biblioteca:
    print(livro)  # Itera sobre os livros após a remoção
