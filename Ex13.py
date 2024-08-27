#
class DivisaoPorZeroError(Exception):
    def __init__(self, mensagem="Erro: Divisão por zero não é permitida."):
        self.mensagem = mensagem
        super().__init__(self.mensagem)


class Divisao:
    @staticmethod
    def dividir(dividendo, divisor):
        if divisor == 0:
            raise DivisaoPorZeroError()  # Lançar exceção personalizada
        return dividendo / divisor

# Exemplo de uso
try:
    resultado = Divisao.dividir(10, 2)
    print(f"O resultado da divisão é: {resultado}")
    
    # Testando a divisão por zero
    resultado = Divisao.dividir(10, 0)
    print(f"O resultado da divisão é: {resultado}")
except DivisaoPorZeroError as e:
    print(e)  # Imprime a mensagem da exceção personalizada
