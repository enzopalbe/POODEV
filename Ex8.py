# Classe Aluno
class Aluno:
    def __init__(self, nome, matricula, nota):
        self.nome = nome
        self.matricula = matricula
        self.nota = nota

    def exibir_informacoes(self):
        print(f"Nome: {self.nome}, Matrícula: {self.matricula}, Nota: {self.nota:.2f}")

# Classe Escola
class Escola:
    def __init__(self, nome):
        self.nome = nome
        self.alunos = []  # Lista para armazenar objetos da classe Aluno

    def adicionar_aluno(self, aluno):
        if isinstance(aluno, Aluno):
            self.alunos.append(aluno)
            print(f"Aluno {aluno.nome} adicionado à escola {self.nome}.")
        else:
            print("Erro: O objeto adicionado não é um Aluno.")

    def exibir_alunos(self):
        print(f"Alunos da escola {self.nome}:")
        for aluno in self.alunos:
            aluno.exibir_informacoes()

# Exemplo de uso:
aluno1 = Aluno("Diogo Siqueira", "12345", 8.5)
aluno2 = Aluno("Enzo Alberoni", "67890", 9.0)

escola = Escola("Escola Primária")
escola.adicionar_aluno(aluno1)
escola.adicionar_aluno(aluno2)

escola.exibir_alunos()
