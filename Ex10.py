from abc import ABC, abstractmethod
import math


class FormaGeometrica(ABC):
    @abstractmethod
    def calcularArea(self):
        pass


class Quadrado(FormaGeometrica):
    def __init__(self, lado):
        self.lado = lado

    def calcularArea(self):
        return self.lado * self.lado


class Circulo(FormaGeometrica):
    def __init__(self, raio):
        self.raio = raio

    def calcularArea(self):
        return math.pi * (self.raio ** 2)

# Exemplo de uso
quadrado = Quadrado(5)
circulo = Circulo(5)

print(f"A área do quadrado é: {quadrado.calcularArea()}")  # Saída: A área do quadrado é: 25
print(f"A área do círculo é: {circulo.calcularArea():.2f}")  # Saída: A área do círculo é: 78.54
