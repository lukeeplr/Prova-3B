def binary_search(arr, key):
    tam = len(list(arr))
    mid = (tam // 2)
    if (arr[mid] == key):   return True
    elif (tam == 1):    return False
    else:
        if (key < arr[mid]):    return binary_search(arr[:mid], key)
        else:   return binary_search(arr[(mid + 1):], key)
