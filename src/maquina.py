from espiral import Espiral

class Maquina:

    def __init__(self, qtdEspirais: int, maximoProdutos: int):
        self.espirais = [Espiral()] * qtdEspirais
        self.qtdEspirais = qtdEspirais
        self.maximoProdutos = maximoProdutos
        self.faturamento = 0
        self.saldo = 0
        self.troco = 0

    def getFaturamento(self) -> float:
        return self.faturamento

    def getMaximoProdutos(self) -> int:
        return self.maximoProdutos

    def getSaldoCliente(self) -> float:
        return self.saldo

    def getSizeEspirais(self) -> int:
        return self.qtdEspirais

    def getEspiral(self, indice: int) -> Espiral:
        if 0 <= indice < len(self.espirais):
            produto = self.espirais[indice]
            if produto.getQuantidade() == 0:
                self.limparEspiral(indice)
            return produto
        return None

    def inserirDinheiro(self, value: float) -> bool:
        if value > 0:
            self.saldo += value
            return True
        else:
            return False

    def receberTroco(self) -> float:
        if self.troco == 0:
            troco = self.saldo
            self.saldo = 0
            return troco
        return self.troco

    def alterarEspiral(self, indice: int, nome: str, quantidade: int, preco: float) -> bool:
        if 0 <= indice < len(self.espirais) and quantidade <= self.maximoProdutos:
            espiral = Espiral()
            espiral.setNomeDoProduto(nome)
            espiral.setQuantidade(quantidade)
            espiral.setPreco(preco)
            self.espirais[indice] = espiral
            return True
        else:
            return False

    def limparEspiral(self, indice: int) -> bool:
        if 0 <= indice < len(self.espirais):
            espiral = self.espirais[indice]
            espiral.setNomeDoProduto(' - ')
            espiral.setQuantidade(0)
            espiral.setPreco(0)
            return True
        else:
            return False

    def vender(self, indice: int) -> bool:
        if 0 <= indice < len(self.espirais):
            produto = self.espirais[indice]
            if produto.getQuantidade() >= 0 and produto.getPreco() <= self.saldo:
                self.troco = round(self.saldo - produto.getPreco(), 2)
                self.saldo -= produto.getPreco()
                produto.setQuantidade(produto.getQuantidade() - 1)
                self.faturamento += produto.getPreco()
                return True
            else:
                return False
        else:
            return False