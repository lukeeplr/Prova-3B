def selection_sort(lista):
    tam = len(lista)
    for c in range(tam-1):
        menori = c
        for x in range(c+1,tam):
            if lista[x] < lista[menori]:
                menori = x
        if c != menori:
            lista[c], lista[menori] = lista[menori], lista[c]
    return lista