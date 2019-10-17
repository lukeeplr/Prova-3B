from random import randint

def quicksort(array):
    tam = len(array)
    if tam < 2:
        return array
    menor, igual, maior = [], [], []
    pivot = array[randint(0, tam-1)]
    for x in array:
        if x < pivot: menor.append(x)
        elif x > pivot: maior.append(x)
        else: igual.append(x)
    return (quicksort(menor) + igual + quicksort(maior))
