def getpivot(arr, c, f):
        m = (c + f) // 2
        pivot = f
        if (arr[c] < arr[m]):
            if (arr[c] < arr[f]):
                pivot = m
        elif (arr[c] < arr[f]):
                pivot = c
        return pivot


def quicksort(array):
    tam = len(array)
    if tam < 2:
        return array
    menor, igual, maior = [], [], []
    pivot = array[getpivot(array, 0, len(array) - 1)]
    for x in array:
        if x < pivot: menor.append(x)
        elif x > pivot: maior.append(x)
        else: igual.append(x)
    return (quicksort(menor) + igual + quicksort(maior))


###########################################################


def quicker(arr):
    return quick(arr, 0, len(arr)-1)


def quick(arr, c, f):
    if c < f:
        p = partition(arr,c,f)
        quick(arr, c, p - 1)
        quick(arr,p + 1, f)
    return arr


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