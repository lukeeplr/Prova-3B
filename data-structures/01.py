class Pilha:
    def __init__(self, maxsize):
        self.top = 0
        self.maxsize = maxsize
        self.items = [None]*maxsize

    empty = lambda self : (self.items == [])
    lenght = lambda self : len(self.items)

    def push(self, item):
        if (self.top != self.maxsize):
            self.items[self.top] = item
            self.top += 1
        else:
            raise Exception ('Pilha cheia')

    def pop(self):
        if not self.empty():
            self.top -= 1
            aux = self.items[self.top]
            self.items[self.top] = None
            return aux
        else: raise Exception ('Pilha vazia')

    def show(self):
        for item in self.items[::-1]:
            if item != None:
                print(item)

def stringmodify(string):
    string = string.replace(' ', '')
    string = string.lower()
    return string

def palindromo(pilha, string):
    t = pilha.maxsize // 2
    for x in range(t):
        if (pilha.pop() != string[x]): return False
    return True

def main():
    strings = [
    'A base do teto desaba',
    'A dama admirou o rim da amada',
    'Anotaram a data da maratona'
]
    for string in strings:
        string = stringmodify(string)
        t = len(string)
        p = Pilha(t)
        for x in string:
            p.push(x)
        print(palindromo(p, string))

main()
