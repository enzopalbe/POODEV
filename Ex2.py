class ContaBancaria:
    def __init__(self, saldo_inicial=0):
        self.__saldo = saldo_inicial  # Atributo privado

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("O valor do depósito deve ser positivo.")

    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso.")
        else:
            print("Saldo insuficiente ou valor inválido para saque.")

    def consultar_saldo(self):
        print(f"Saldo atual: R${self.__saldo:.2f}")


# Exemplo de uso:
conta = ContaBancaria(900)
conta.depositar(500)
conta.sacar(300)
conta.consultar_saldo()
