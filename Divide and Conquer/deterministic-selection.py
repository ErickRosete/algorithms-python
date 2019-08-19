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

def choosePivot(arr):
    c = []
    i = 0
    auxArr = []
    
    for num in arr:
        auxArr.append(num)
        i += 1
        if(i == 5):
            auxArr = mergeSort(auxArr)
            c.append(auxArr[i//2])
            i = 0
            auxArr = []
    
    if(i > 0):
        auxArr = mergeSort(auxArr)
        c.append(auxArr[i//2])
    
    pivot = DSelection(c, len(c)//2)
    return pivot
  
def DSelection(arr, pos):
    n = len(arr)
    if(pos > n):
        return -1
    if(n == 1):
        return arr[0]
    
    pivot = choosePivot(arr)
    l = 0
    r = 0
    for j in range(n):            
        if(arr[j] < pivot):
            arr[j], arr[l] = arr[l], arr[j]
            if(r > l):
                arr[r], arr[j] = arr[j], arr[r]
            l += 1
            r += 1
        elif(arr[j] == pivot):
            arr[j], arr[r] = arr[r], arr[j]
            r += 1
    
    if(l <= pos - 1 and r > pos - 1):
        return arr[l]
    elif(l > pos - 1):
        return DSelection(arr[:l], pos)
    else:
        return DSelection(arr[r:], pos - r)

arr = [random.randint(1, 20) for _ in range(20)]
pos = random.randint(1, len(arr))
sortedArray = mergeSort(arr)
print(sortedArray[pos-1])
print(DSelection(arr, pos))
