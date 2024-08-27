from typing import List, Optional

# Classe Funcionario


class Funcionario:
    def __init__(self, id: int, nome: str, cargo: str, salario: float):
        self.id = id
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

    def __str__(self) -> str:
        return f"ID: {self.id}, Nome: {self.nome}, Cargo: {self.cargo}, Salário: R${self.salario:.2f}"

# Classe GerenciadorFuncionarios


class GerenciadorFuncionarios:
    def __init__(self):
        self.funcionarios: List[Funcionario] = []

    def adicionar_funcionario(self, id: int, nome: str, cargo: str, salario: float) -> None:
        funcionario = Funcionario(id, nome, cargo, salario)
        self.funcionarios.append(funcionario)
        print(f"Funcionário '{nome}' adicionado com sucesso.")

    def remover_funcionario(self, id: int) -> None:
        funcionario = self._buscar_funcionario_por_id(id)
        if funcionario:
            self.funcionarios.remove(funcionario)
            print(f"Funcionário com ID {id} removido com sucesso.")
        else:
            print(f"Funcionário com ID {id} não encontrado.")

    def atualizar_funcionario(self, id: int, nome: Optional[str] = None, cargo: Optional[str] = None, salario: Optional[float] = None) -> None:
        funcionario = self._buscar_funcionario_por_id(id)
        if funcionario:
            if nome:
                funcionario.nome = nome
            if cargo:
                funcionario.cargo = cargo
            if salario is not None:
                funcionario.salario = salario
            print(f"Funcionário com ID {id} atualizado com sucesso.")
        else:
            print(f"Funcionário com ID {id} não encontrado.")

    def listar_funcionarios(self) -> None:
        if not self.funcionarios:
            print("Nenhum funcionário cadastrado.")
        else:
            print("Lista de Funcionários:")
            for funcionario in self.funcionarios:
                print(funcionario)

    def _buscar_funcionario_por_id(self, id: int) -> Optional[Funcionario]:
        for funcionario in self.funcionarios:
            if funcionario.id == id:
                return funcionario
        return None


# Exemplo de uso
gerenciador = GerenciadorFuncionarios()

# Adicionar funcionários
gerenciador.adicionar_funcionario(
    123456, "Gabriel Costa", "Faxineiro", 1412.00)
gerenciador.adicionar_funcionario(
    567890, "Enzo Alberoni", "Analista", 65000.00)
gerenciador.adicionar_funcionario(
    748173, "Diogo Siqueira", "Cozinheiro", 1600.00)

# Listar funcionários
gerenciador.listar_funcionarios()

# Atualizar funcionário
gerenciador.atualizar_funcionario(123456, salario=2000.00)

# Listar funcionários novamente
gerenciador.listar_funcionarios()

# Remover funcionário
gerenciador.remover_funcionario(748173)

# Listar funcionários novamente
gerenciador.listar_funcionarios()
