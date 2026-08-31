class Produto:
    def __init__ (self, nome: str, preco: float, quantidade: int = 0):
        self.nome = nome
        self._preco = preco
        if quantidade < 0:
            raise ValueError('Quantidade inválida!')
        else:
            self.quantidade = quantidade

    def repr(self):
        formato = f'Produto(nome={self.nome}, preco={self._preco}, quantidade={self.quantidade})'
        Produto(nome ='Detergente')
        return formato

    def str(self):
        formato = f'Nome......: {self.nome}\n' + \
                  f'Preço.....:{self._preco:.2f}\n' + \
                  f'Quantidade:{self.quantidade}'
        return formato

    def get_preco(self):
        return self._preco

    def set_preco(self, valor):
        self.preco = valor

    @property
    def qtd(self):
        return self.quantidade

    @qtd.setter
    def qtd(self, valor):
        if valor >= 0:
            self.quantidade = valor
        else:
            raise ValueError('Quantidade não pode ser negativa!')

def main():
    p1 = Produto('Detergente', 4.0, 5)
    print(p1)
    p1.qtd = 3 * p1.qtd
    print(p1)

if __name__ == '__main__':
    main()