
#arr : list
#n   : what you want to find

def binarySearch(arr, n):  #return bool
    arr.sort()

    while len(arr) >= 1:
        length = len(arr)

        if arr[length // 2] == n:
            return True

        elif n < arr[length // 2]:
            arr = arr[:length // 2]
            
        elif n > arr[length // 2]:
            arr = arr[length // 2 + 1:]

    return False

