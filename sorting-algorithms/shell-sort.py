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
    h = getH(tam)
    while h > 0:
        for x in range(h,tam):
            z = arr[x]
            y = x
            while arr[y - h] > z:
                arr[y] = arr[y - h]
                y -= 1
                if y < h:
                    break
                arr[y] = z
        h //= 3
    return arr
