
class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def info(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}")


class Carro(Veiculo):
    def __init__(self, marca, modelo, numero_de_portas, tipo_de_combustivel):
        super().__init__(marca, modelo) 
        self.numero_de_portas = numero_de_portas
        self.tipo_de_combustivel = tipo_de_combustivel

    def info(self):
        super().info()  
        print(f"Número de Portas: {self.numero_de_portas}, Tipo de Combustível: {self.tipo_de_combustivel}")

    def ligar(self):
        print(f"O carro {self.modelo} está ligado.")

    def desligar(self):
        print(f"O carro {self.modelo} está desligado.")

# Exemplo de uso:
carro1 = Carro("Chevrolet", "Cruze", 4, "Diesel")
carro1.info()
carro1.ligar()
carro1.desligar()
