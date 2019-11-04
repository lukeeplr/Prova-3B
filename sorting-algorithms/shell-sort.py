def getH(n):
    h = 1
    while (h < n):
        if (3 * h) + 1 < n:
            h = (3 * h) + 1
        else:
            break
    return h


def shell_sort(arr): 
    tam = len(arr) 
    gap = getH(tam)
    while gap > 0: 
        for x in range(gap,tam): 
            temp = arr[x] 
            y = x 
            while  y >= gap and arr[y-gap] >temp: 
                arr[y] = arr[y-gap] 
                y -= gap 
            arr[y] = temp 
        gap //= 3
    return arr
