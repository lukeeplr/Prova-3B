class Node:
    def __init__(self, item):
        self.item = item
        self.prox = None

class Queue:
    def __init__(self):
        self.tamanho = 0
        self.inicio = None
        self.final = None

    vazia = lambda self : (self.tamanho == 0)

    def enfileirar(self, item):
        if (self.vazia()):
            self.inicio = Node(item)
            self.final = self.inicio
        else:
            self.final.prox = Node(item)
            self.final = self.final.prox
        self.tamanho += 1

    def desenfileirar(self):
        if (not self.vazia()):
            aux = self.inicio
            self.inicio = self.inicio.prox
            item = aux.item
            del aux
            self.tamanho -= 1
            return item
        else:
            raise Exception ('Não é possível desenfileirar filas vazias')

    def imprimir(self):
        aux = self.inicio
        print('-=-')
        while aux != None:
            print(aux.item, end = " ")
            aux = aux.prox
        print()
        print('-=-')
