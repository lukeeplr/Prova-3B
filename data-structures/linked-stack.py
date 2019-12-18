class Cell:
    item = None
    prox = None

    def __init__(self, item):
        self.item = item


class Stack:
    top = None
    tam = None

    def __init__(self):
        self.tam = 0

    empty = lambda self : (self.tam == 0)

    def push(self, item):
        c = Cell(item)
        aux = self.top
        self.top, self.top.prox = c, aux
        self.tam += 1

    def pop(self):
        if not self.empty():
            aux = self.top
            self.top = self.top.prox
            item = aux.item
            del aux
            self.tam -= 1
            return item

        else: raise Exception ('Pilha vazia')

    def show(self):
        aux = self.top
        print('-=-')
        while (aux != None):
            print(aux.item)
            aux = aux.prox
        print('-=-')


p = Stack()
p.push(5)
p.push(8)
p.push(6)
p.show()
for c in range(3): '''desempilhar tudo'''
    p.pop()
p.push(1)
p.show()
