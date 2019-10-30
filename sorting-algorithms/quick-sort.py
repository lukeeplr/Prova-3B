def quickSort(arr):
    tam = len(arr)
    if (tam < 2): return arr
    pivp = getpivot(arr, 0, tam - 1)
    pivot = arr[pivp]
    menor, igual, maior = [], [], []
    for number in arr:
        if (number < pivot):    menor.append(number)
        elif (number > pivot):  maior.append(number)
        else:   igual.append(number)
    return (quickSort(menor) + igual + quickSort(maior))


def getpivot(arr, c, f):
        m = (c + f) // 2
        pivot = f
        if (arr[c] < arr[m]):
            if (arr[c] < arr[f]):
                pivot = m
        elif (arr[c] < arr[f]):
                pivot = c
        return pivot


def partition(arr, c, f):
    p = getpivot(arr, c, f)
    arr[p], arr[f] = arr[f], arr[p]
    pivot = arr[f]
    x = c - 1
    for y in range(c,f):
        if arr[y] < pivot:
            x += 1
            arr[x],arr[y] = arr[y], arr[x]
    arr[x + 1], arr[f] = arr[f], arr[x + 1]
    return (x+1)


def quick(arr, c, f):
    if c < f:
        p = partition(arr,c,f)
        quick(arr, c, p - 1)
        quick(arr,p + 1, f)
    return arr


def quicker(arr):
    return quick(arr, 0, len(arr)-1)
