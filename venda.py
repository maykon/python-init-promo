class Venda():

    def __init__(self, terminal, produtos = []):
      self.terminal = terminal
      self.produtos = produtos

    def adicionar_produto(self, produto):
        if produto:
            produto
            self.produtos.append(produto)

    def remover_produto(self, produto):
        if produto:
            self.produtos.remove(produto)

    def finalizar_venda(self):
        pass