def binary_search(arr, key):
    mid = (len(arr) // 2)
    if key == arr[mid]:
        return True
    elif mid == 1:
        return False
    else:
        if key < arr[mid]:
            return binary_search(arr[:mid], key)
        else:
            return binary_search(arr[(mid +1):], key)