class Calculadora:
    def adicionar(self, *numeros):
        return sum(numeros)

    def subtrair(self, a, *numeros):
        resultado = a
        for num in numeros:
            resultado -= num
        return resultado

    def multiplicar(self, *numeros):
        if not numeros:
            return 0
        resultado = 1
        for num in numeros:
            resultado *= num
        return resultado

    def dividir(self, a, *numeros):
        resultado = a
        for num in numeros:
            if num != 0:
                resultado /= num
            else:
                return "Erro: Divisão por zero"
        return resultado


# Exemplo de uso:
calc = Calculadora()

# Operações com diferentes números de parâmetros:
print(calc.adicionar(5, 5, 7, 4))  # 21
print(calc.subtrair(20, 6, 1))      # 13
print(calc.multiplicar(3, 3, 4))    # 36
print(calc.dividir(100, 2, 10))      # 5.0
