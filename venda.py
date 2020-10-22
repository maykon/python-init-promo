from terminal import Terminal
import socket
from produto import Produto
from mensagem_venda import MensagemVenda

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
        mensagem_venda = MensagemVenda(self)
        mensagem_venda.to_xml()


if __name__ == "__main__":
    terminal = Terminal('psts', '9906', socket.gethostname())
    venda = Venda(terminal, [Produto(1, 5.5)])
    venda.finalizar_venda()