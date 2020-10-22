import dict2xml

class MensagemProduto():

  def __init__(self, produto, seq, quantidade):
    self.seq = seq
    self.code = produto.codigo
    self.qty = quantidade
    self.unitprice = produto.valor_unitario
    self.xprice = produto.valor_unitario * quantidade

  def to_xml(self):
    mensagem = self.__dict__
    xml = dict2xml(mensagem, wrap="all", indent="  ")
    