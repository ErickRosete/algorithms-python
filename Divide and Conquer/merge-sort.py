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

print(mergeSort([5, 4, 1, 8, 6, 3, 9, 12, 7, 2, 6, 2, 7.5]))