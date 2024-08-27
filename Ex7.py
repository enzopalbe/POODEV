
class Motor:
    def __init__(self):
        self.ligado = False  # O motor começa desligado

    def ligar(self):
        if not self.ligado:
            self.ligado = True
            print("Motor ligado.")
        else:
            print("O motor já está ligado.")

    def desligar(self):
        if self.ligado:
            self.ligado = False
            print("Motor desligado.")
        else:
            print("O motor já está desligado.")

    def status(self):
        return "ligado" if self.ligado else "desligado"


class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.motor = Motor()  # O carro tem um motor

    def ligar_motor(self):
        self.motor.ligar()

    def desligar_motor(self):
        self.motor.desligar()

    def verificar_status_motor(self):
        status = self.motor.status()
        print(f"O motor está {status}.")

    def exibir_informacoes(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}")


# Exemplo de uso
carro = Carro("Toyota", "Corolla")
carro.exibir_informacoes()
carro.verificar_status_motor()
carro.ligar_motor()
carro.verificar_status_motor()
carro.desligar_motor()
carro.verificar_status_motor()
