import random

def mergeSort(arr):
    if(len(arr) == 1):
        return arr
    
    arr1 = mergeSort(arr[:len(arr)//2])
    arr2 = mergeSort(arr[len(arr)//2:])
    ind1 = 0
    ind2 = 0
    newArray = []
    for i in range(len(arr)):
        if(ind2 >= len(arr2) or (ind1 < len(arr1) and arr1[ind1] < arr2[ind2])):
            newArray.append(arr1[ind1])
            ind1 += 1
        else:
            newArray.append(arr2[ind2])
            ind2 += 1
    return newArray

def randomizedSelection(arr, pos):
    n = len(arr)
    if(pos > n):
        return -1
    if(n == 1):
        return arr[0]
    
    indexPivot = random.randint(0, n-1)
    arr[0] , arr[indexPivot] = arr[indexPivot], arr[0]
    pivot = arr[0]
    
    i = 1
    for j in range(1, n):
        if(arr[j] < pivot):
            arr[j], arr[i] = arr[i], arr[j]
            i += 1
    
    arr[i-1], arr[0] = arr[0], arr[i-1]
    
    if(i == pos):
        return arr[i-1]
    elif(i > pos):
        return randomizedSelection(arr[:i-1], pos)
    else:
        return randomizedSelection(arr[i:], pos - i)

arr = [20,45,5,21,41,62,10,2,30,12,73,84,16,48,7,1,319,3,552,23,34,23,4,6,71245,123]
pos = random.randint(1, len(arr))
sortedArray = mergeSort(arr)
print(sortedArray[pos-1])
print(randomizedSelection(arr, pos))
