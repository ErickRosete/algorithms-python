import random;
def memoryQuickSort(arr):
    n = len(arr)
    if(n <= 1):
        return arr
    
    pivotInd = random.randint(0,n-1)
    pivot = arr[pivotInd]
    l = 0
    r = n - 1
    newArray = [0] * n
    pivotTimes = 0
    
    for i in range(n):
        if(arr[i] < pivot):
            newArray[l] = arr[i]
            l += 1
        elif(arr[i] > pivot):
            newArray[r] = arr[i]
            r -= 1
        else:
            pivotTimes += 1
    
    for i in range(pivotTimes):
        newArray[i + l] = pivot

    sortedArray = memoryQuickSort(newArray[:l]) + newArray[l:r+1] + memoryQuickSort(newArray[r+1:])
    return sortedArray

def altQuickSort(arr, l_ref, r_ref):
    if(r_ref - l_ref <= 1):
        return arr
    
    pivotInd = random.randint(l_ref, r_ref - 1)
    arr[l_ref], arr[pivotInd] = arr[pivotInd], arr[l_ref]
    pivot = arr[l_ref]
    l = l_ref + 1
    i = l_ref + 1
    r = r_ref - 1
    
    for j in range(l_ref + 1, r_ref):            
        if(arr[i] < pivot):
            arr[i], arr[l] = arr[l], arr[i]
            l += 1
            i += 1
        elif(arr[i] > pivot):
            arr[i], arr[r] = arr[r], arr[i]
            r -= 1
        else:
            i += 1
    arr[l_ref], arr[l-1] = arr[l-1], arr[l_ref]
    
    altQuickSort(arr, l_ref, l-1)
    altQuickSort(arr, r, r_ref)   

def quickSort(arr, l_ref, r_ref):
    if(r_ref - l_ref <= 1):
        return arr
    
    pivotInd = random.randint(l_ref, r_ref - 1)
    arr[l_ref], arr[pivotInd] = arr[pivotInd], arr[l_ref]
    pivot = arr[l_ref]
    l = l_ref + 1
    r = l_ref + 1
    
    for j in range(l_ref + 1, r_ref):            
        if(arr[j] < pivot):
            arr[j], arr[l] = arr[l], arr[j]
            if(r > l):
                arr[r], arr[j] = arr[j], arr[r]
            l += 1
            r += 1
        elif(arr[j] == pivot):
            arr[j], arr[r] = arr[r], arr[j]
            r += 1
    arr[l_ref], arr[l-1] = arr[l-1], arr[l_ref]
    
    quickSort(arr, l_ref, l-1)
    quickSort(arr, r, r_ref)    

arr = [random.randint(1, 20) for _ in range(20)]
altQuickSort(arr, 0, len(arr))
print(arr)
arr2 = [random.randint(1, 20) for _ in range(20)]
quickSort(arr2, 0, len(arr2))
print(arr2)
#print(memoryQuickSort(arr))
#print(altQuickSort(arr))

