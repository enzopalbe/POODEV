class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def info(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}")


# Exemplo de uso:
pessoa = Pessoa("Enzo", 20)
pessoa.info()
