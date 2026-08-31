from produto import *

class CarrinhoDeCompras:
    def __init__(self):
        self.__itens = []

    def adicionaItem(self, item: Produto):
        self.__itens.append(item)

    #def removerItem(self, nome: str): -> opção para remover o item do carrinho 
    #                                     utilizando o nome como parametro da função
    #    self.__itens = [item for item in self.__itens if item.nome != nome]
    def removerItem(self, item: Produto):
        self.__itens = [i for i in self.__itens if i.nome != item.nome]

    def __repr__(self):
        formato = 'CarrinhoDeCompras('
        for item in self.__itens:
            formato += str(item)
        formato += '\n)'
        return formato

    def __str__(self):
        formato = '🛒 (CarrinhoDeCompras)\n'
        formato += '-' * 23 + '\n'
        if self.__itens == []:
            formato += 'Vazio'
        else:
            for item in self.__itens:
                formato += f'Nome......: {item.nome}\n'
                formato += f'Preco.....: R$ {item.get_preco():.2f}\n'
                formato += f'Quantidade: {item.qtd}\n' 
        formato += '-' * 23 + '\n'
        return formato

def main():
    c1 = CarrinhoDeCompras()
    p1 = Produto('Iphone 17', 5000.00, 2)
    p2 = Produto('Fone de ouvido', 200.00, 1)
    p3 = Produto('Macbook', 8000.00, 3)
    print(c1)
    print()
    c1.adicionaItem(p1)
    print(c1)
    c1.adicionaItem(p2)
    print(c1)
    c1.removerItem(p1)
    print(f'Carrinho atualizado: {c1}')


if __name__ == '__main__':
    main()