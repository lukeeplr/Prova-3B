def binary_search_recursive(arr, key):
    tam = len(arr)
    mid = (tam // 2)
    if (arr[mid] == key):   return True
    elif (tam == 1):    return False
    else:
        if (key < arr[mid]):    return binary_search(arr[:mid], key)
        else:   return binary_search(arr[(mid + 1):], key)



def binary_search(arr, key):
    start = 0
    end = len(arr) - 1
    mid = (start + end // 2)

    while ((arr[mid] != key) and (start <= end)):
        
        if (key < arr[mid]):
            end = mid - 1
        
        else:
            start = mid + 1

        mid = ((start + end) // 2)

    if (arr[mid] == key):
        return True
    else:
        return False
