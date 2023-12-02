class Espiral:

    def __init__(self):
        self.nomeProdutos = ' - '
        self.qtdProdutos = 0
        self.preco = 0

    def getNomeDoProduto(self):
        return self.nomeProdutos

    def setNomeDoProduto(self, nome):
        self.nomeProdutos = nome
        return self.nomeProdutos

    def getPreco(self):
        return self.preco

    def setPreco(self, preco):
        self.preco = preco
        return self.preco

    def getQuantidade(self):
        return self.qtdProdutos

    def setQuantidade(self, quantidade):
        self.qtdProdutos = quantidade
        return self.qtdProdutos