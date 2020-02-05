class Node:
    def __init__(self, item):
        self.item  = item
        self.proximo = None


class LinkedList:
    def __init__(self):
        self.inicio = None
        self.quantidade = 0


    def empty(self):
        return self.quantidade == 0


    def inserir(self, pos, item):
        if self.empty():
            self.inicio = Node(item)
            self.quantidade += 1
        else:
            if (pos <= self.quantidade + 1):
                p = self.inicio
                for _ in range(pos - 1):
                    p = p.proximo
                aux = Node(item)
                aux.proximo = p.proximo
                p.proximo = aux
                self.quantidade += 1
            else:
                raise Exception ('Operação inválida')


    def remover(self, pos):
        if not self.empty():
            if (pos <= self.quantidade):
                if (pos == 0):
                    aux = self.inicio
                    self.inicio = aux.proximo
                    item = aux.item
                    del aux
                    self.quantidade -= 1
                    return item
                else:
                    p = self.inicio
                    for _ in range(pos-1):
                        p = p.proximo
                    aux = p.proximo
                    item = aux.item
                    p.proximo = aux.proximo
                    self.quantidade -=1
                    del aux
                    return item
            else:
                raise Exception ('Operação inválida')
        else:
            raise Exception ('Operação inválida')


    def imprimir(self):
        p = self.inicio
        while (p != None):
            print(p.item, end = ' ')
            p = p.proximo
        print('\n---')

