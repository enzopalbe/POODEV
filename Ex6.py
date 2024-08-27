# Classe base Animal
class Animal:
    def emitirSom(self):
        raise NotImplementedError(
            "O método emitirSom deve ser sobrescrito nas subclasses")


class Cachorro(Animal):
    def emitirSom(self):
        return "Au Au"


class Gato(Animal):
    def emitirSom(self):
        return "Miauuu"
# Exemplo de uso:


def fazer_animais_emitir_som(animais):
    for animal in animais:
        print(animal.emitirSom())


# Criando instâncias de Cachorro e Gato
cachorro = Cachorro()
gato = Gato()

# Fazendo os animais emitir som
fazer_animais_emitir_som([cachorro, gato])
