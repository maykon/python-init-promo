from produto import Produto

class Carrinho():
    def __init__(self, store_id, terminal, venda):
        self.companyId = 'psts'
        self.store_id = store_id
        self.terminal = terminal
        self.venda = venda

    def adicionar_produto(self, produto):
        self.venda.adicionar_produto(produto)
        salvar()
        
    def remover_produto(self, produto):
        self.venda.remover_produto(produto)
        salvar()

    def finalizar_venda(self):
        self.venda.finalizar_venda()
        salvar()
    
    def salvar(self):
        pass
