class Pilha:
    def __init__(self, items, maxsize):
        self.items = items
        self.top = 0
        self.maxsize = maxsize

    empty = lambda self : (self.items == [])
    lenght = lambda self : len(self.items)

    def push(self, item):
        if (self.top != self.maxsize):
            self.items.insert(self.top, item)
            self.top += 1
        else:
            raise Exception ('Pilha cheia')

    def pop(self):
        if (self.empty()):
            return self.items
        else:
            del self.items[self.top - 1]
            self.top -= 1
