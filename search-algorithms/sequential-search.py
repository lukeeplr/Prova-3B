def sequential_search(arr, key):
    n = len(arr)
    found = False
    x = 0
    while (x < n) and (not found):
        if (arr[x] == key):   found = True
        else:   x += 1
    return found


def sequencial_recursiva(lista, chave, indice = 0):

    if (indice == len(lista)):
        return False
    
    elif (chave == lista[indice]):
        return True
    
    else:
        return sequencial_recursiva(lista, chave, indice + 1)
