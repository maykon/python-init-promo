import datetime

class MensagemVenda():
  
  def __init__(self, venda, message_id = 1, init_ticket = True):
    self.mensagem = {
      '@companyId': venda.terminal.company_id,
      '@store': venda.terminal.store,
      '@terminal': venda.terminal.terminal,
      '@datetime': datetime.today(),
      '@messageId': message_id,
      '@sugest': 'true',
      '@response': 'true',
      '@init-tck': 'true' if init_ticket else 'false',
      '@evaluate': 'true',
      '@msg-version': '2.4'
    }