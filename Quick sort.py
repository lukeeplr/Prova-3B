def partition(array):
    tam = len(array)
    pivot = (tam // 2) - 1
    array[pivot], array[-1] = array[-1], array[pivot]
    left = 0
    right = tam - 2
    while left <= right:
        while array[left] < array[-1]:
            left += 1
        while array[right] > array[-1]:
            right -= 1
        array[left], array[right] = array[right], array[left]
    if left == right:
        left += 1
        right -= 1
    array[left], array[-1] = array[-1], array[left]
    return array


lista = [2, 6, 5, 3, 8, 7, 1, 0]
lista2 = [8, 7, 6, 5]
print(partition(lista2))