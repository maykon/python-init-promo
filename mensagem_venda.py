import datetime
import xmltodict
from mensagem_produto import MensagemProduto


class MensagemVenda():
  
  def __init__(self, terminal, message_id = 1, init_ticket = True):
    self.terminal = terminal
    self.message_id = message_id

  def obter_mensagem_venda(self, init_ticket):
    return {
      'message': {
        '@companyId': self.terminal.company_id,
        '@store': self.terminal.store,
        '@terminal': self.terminal.terminal,
        '@datetime': datetime.datetime.now(),
        '@messageId': self.message_id,
        '@suggest': 'true',
        '@response': 'true',
        '@init-tck': 'true' if init_ticket else 'false',
        '@evaluate': 'true',
        '@msg-version': '2.4'        
      }
    }
  
  def obter_mensagem_produto(self, produto, seq, qtde, init_ticket = False):
    mensagem = self.obter_mensagem_venda(init_ticket)
    mensagem_produto = MensagemProduto(produto, seq, qtde)

    mensagem['message']['item-add'] = mensagem_produto.obter_mensagem_produto()
    return xmltodict.unparse(mensagem, pretty=True)