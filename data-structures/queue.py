class Fila:
    def __init__(self, tam):
        self.tam = tam
        self.fila = [None for x in range(tam)]
        self.inic = self.fim = -1
        

    def enfileirar(self, item):
        if (((self.fim + 1) % self.tam) == self.inic): raise Exception ('Fila cheia')

        elif (self.inic == -1):
            self.inic = 0
            self.fim = 0
            self.fila[self.fim] = item

        else:
            self.fim = (self.fim + 1) % self.tam 
            self.fila[self.fim] = item

    def desenfileirar(self):
        if (self.inic == -1): raise Exception ('Fila vazia')

        elif (self.inic == self.fim):
            aux = self.fila[self.inic]
            self.fila[self.inic] = None
            self.inic -= 1
            self.fim -= 1
            return aux

        else:
            aux = self.fila[self.inic]
            self.fila[self.inic] = None
            self.inic = (self.inic + 1) % self.tam
            return aux

    def mostrar(self):
        if (self.inic == -1): print('Fila vazia')

        elif (self.fim >= self.inic):
            for x in range(self.inic, self.fim + 1):
                print(self.fila[x], end = ' ')
            print()

        else:
            for x in range(self.inic, self.tam):
                print(self.fila[x], end = ' ')
            for x in range(0, self.fim + 1):
                print(self.fila[x], end = ' ')
            print()
