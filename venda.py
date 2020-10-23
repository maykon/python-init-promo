from terminal import Terminal
import socket
from produto import Produto
from mensagem_venda import MensagemVenda
from consulta_promo import ConsultaPromo

class Venda():
  def __init__(self, terminal, produtos = []):
    self.terminal = terminal
    self.produtos = produtos

  def adicionar_produto(self, produto):
    mensagem_venda = MensagemVenda(self.terminal)
    xml = mensagem_venda.obter_mensagem_produto(produto, 1, 20)

    return ConsultaPromo().consultar_promocao(xml)

  def remover_produto(self, produto):
    if produto:
      self.produtos.remove(produto)

  def finalizar_venda(self):
    pass    

if __name__ == "__main__":
  terminal = Terminal('psts', '9906', 'MGA10196')#socket.gethostname()
  venda = Venda(terminal)
  venda.adicionar_produto(Produto('Produto 01', 5.5))


