class Node:
    def __init__(self, item):
        self.item = item
        self.prox = None 


class Lista:
    def __init__(self):
        self.inicio = None
        self.tam = 0



    def append(self, item):
        x = Node(item)

        if (self.inicio == None): 
            self.inicio = x
            self.tam += 1
            return

        p = self.inicio
        while (p.prox != None):
            p = p.prox

        p.prox = x
        self.tam += 1



    def inserir(self, pos, item):
        x = Node(item)
        if (self.inicio == None):
            self.inicio = x

        elif (pos >= self.tam): self.append(item)

        else:
            cont = 1
            aux = self.inicio

            while pos > cont:
                aux = aux.prox
                cont += 1

            x.prox = aux.prox
            aux.prox = x

        self.tam += 1



    def pop(self):
        
        if (self.inicio == None): raise Exception ('Remoção em lista vazia')

        x = self.inicio
        cont = 0

        while (cont < self.tam - 2):
            x = x.prox
            cont += 1

        x.prox = None
        self.tam -= 1



    def show(self):

        aux = self.inicio
        while (aux != None):
            print(aux.item, end = ' ')
            aux = aux.prox
        print()



def main():
    l = Lista()
    l.append(3)
    l.append(5)
    l.append(2)
    l.append(4)
    l.append(8)
    l.pop()
    l.inserir(2, 7)
    l.show()

main()
