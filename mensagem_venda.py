import datetime
import xmltodict

class MensagemVenda():
  
  def __init__(self, venda, message_id = 1, init_ticket = True):
    self.mensagem = 

  def to_xml(self):
    print((xmltodict.unparse(self.mensagem, pretty=True)))

  def obter_mensagem_venda(self, terminal, message_id, init_ticket):
    return {
      'message': {
        '@companyId': terminal.company_id,
        '@store': terminal.store,
        '@terminal': terminal.terminal,
        '@datetime': datetime.datetime.now(),
        '@messageId': message_id,
        '@sugest': 'true',
        '@response': 'true',
        '@init-tck': 'true' if init_ticket else 'false',
        '@evaluate': 'true',
        '@msg-version': '2.4'        
      }
    }
  
  def obter_mensagem_produto(self, produto, seq, qtde):
    mensagem = obter_mensagem_venda(terminal, message_id, False)
    mensagem['message']['item-add'] = {
      '@seq': seq,
      '@code': produto.codigo,
      '@qty': qtde,
      '@unitprice': produto.valor_unitario
      '@xprice': qtde * produto.valor_unitario
    }