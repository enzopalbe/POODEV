from typing import TypeVar, Generic, List


T = TypeVar('T')


class Caixa(Generic[T]):
    def __init__(self):
        self.itens: List[T] = []  # Lista para armazenar itens do tipo T

    def adicionar(self, item: T) -> None:
        """Adiciona um item à caixa."""
        self.itens.append(item)
        print(f"Item '{item}' adicionado à caixa.")

    def remover(self, item: T) -> None:
        """Remove um item da caixa se ele existir."""
        if item in self.itens:
            self.itens.remove(item)
            print(f"Item '{item}' removido da caixa.")
        else:
            print(f"Item '{item}' não encontrado na caixa.")

    def listar(self) -> None:
        """Lista todos os itens na caixa."""
        if not self.itens:
            print("A caixa está vazia.")
        else:
            print("Itens na caixa:")
            for item in self.itens:
                print(item)

# Exemplo de uso com diferentes tipos

# Caixa para armazenar inteiros
caixa_inteiros = Caixa[int]()
caixa_inteiros.adicionar(1)
caixa_inteiros.adicionar(2)
caixa_inteiros.listar()
caixa_inteiros.remover(1)
caixa_inteiros.listar()

# Caixa para armazenar strings
caixa_strings = Caixa[str]()
caixa_strings.adicionar("Pera")
caixa_strings.adicionar("Uva")
caixa_strings.listar()
caixa_strings.remover("Pera")
caixa_strings.listar()
