def sequential_search(arr, key):
    n = len(arr)
    found = False
    x = 0
    while (x <= n) and (not found):
        if (arr[x] == key):   found = True
        else:   x += 1
    return found
