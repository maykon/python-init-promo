class MensagemProduto():

  def __init__(self, produto, seq, quantidade):
    self.seq = seq
    self.code = produto.codigo
    self.qty = quantidade
    self.unitprice = produto.valor_unitario
    self.xprice = produto.valor_unitario * quantidade
  
  def obter_mensagem_produto(self):
    return {
      '@seq': self.seq,
      '@code': self.code,
      '@qty': self.qty,
      '@unitprice': self.unitprice,
      '@xprice': self.xprice
    }
