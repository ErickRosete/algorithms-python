def binarySearch(arr, val):
    n = len(arr)
    if(n == 1):
        if(arr[0] == val):
            return 0
        else:
            return -1
   
    nby2 = n // 2
    if(val == arr[nby2]):
        return nby2
    elif(val < arr[nby2]):
        return binarySearch(arr[:nby2], val)
    else:
        pos = binarySearch(arr[nby2 + 1:], val)
        if(pos >= 0):
            return nby2 + 1 + pos
        else:
            return pos
    

arr = [1,2,3,4,6,7,9,20,23,28,40]
print(binarySearch(arr, 1))
print(binarySearch(arr, 2))
print(binarySearch(arr, 4))
print(binarySearch(arr, 6))
print(binarySearch(arr, 8))
print(binarySearch(arr, 10))
print(binarySearch(arr, 20))
print(binarySearch(arr, 40))