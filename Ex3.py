class Produto:
    def __init__(self, nome, preco, quantidade_em_estoque):
        self.nome = nome
        self.preco = preco
        self.quantidade_em_estoque = quantidade_em_estoque

    def exibir(self):
        print(f"Produto: {self.nome}, Preço: R${
              self.preco:.2f}, Quantidade em Estoque: {self.quantidade_em_estoque}")


# Criação de instâncias da classe Produto:
produto1 = Produto("Computador", 5000.00, 30)
produto2 = Produto("Celular", 3500.00, 20)
produto3 = Produto("Fone de Ouvido", 300.00, 100)

# Exibindo as informações dos produtos:
produto1.exibir()
produto2.exibir()
produto3.exibir()
