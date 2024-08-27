import math


class MatematicaUtil:
    @staticmethod
    def quadrado(numero):

        return numero ** 2

    @staticmethod
    def cubo(numero):

        return numero ** 3

    @staticmethod
    def raiz_quadrada(numero):

        if numero < 0:
            raise ValueError(
                "Não é possível calcular a raiz quadrada de um número negativo.")
        return math.sqrt(numero)


# Exemplo de uso
num = 16
# Saída: O quadrado de 16 é: 256
print(f"O quadrado de {num} é: {MatematicaUtil.quadrado(num)}")
# Saída: O cubo de 16 é: 4096
print(f"O cubo de {num} é: {MatematicaUtil.cubo(num)}")
# Saída: A raiz quadrada de 16 é: 4.0
print(f"A raiz quadrada de {num} é: {MatematicaUtil.raiz_quadrada(num)}")


try:
    MatematicaUtil.raiz_quadrada(-9)
except ValueError as e:
    # Saída: Não é possível calcular a raiz quadrada de um número negativo.
    print(e)
