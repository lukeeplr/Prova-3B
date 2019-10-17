def merge(lista1, lista2):
    lista3 = []
    a = b = 0
    tamA = len(lista1)
    tamB = len(lista2)
    while a < tamA and b < tamB:
        if lista1[a] < lista2[b]:
            lista3.append(lista1[a])
            a += 1
        else:
            lista3.append(lista2[b])
            b += 1
    if a == tamA:   lista3.extend(lista2[b:])
    else:           lista3.extend(lista1[a:])
    return lista3


def merge_sort(lista):
    tam = len(lista)
    if tam <= 1: return lista
    metade1, metade2 = merge_sort(lista[:int(tam/2)]), merge_sort(lista[int(tam/2):])
    return merge(metade1,metade2)