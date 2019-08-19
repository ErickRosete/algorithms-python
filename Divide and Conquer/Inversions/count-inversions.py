def sortCountInv(arr):
    n = len(arr)
    if(n <= 1):
        return arr, 0
    
    nby2 = n // 2
    sortedLeftArr, leftCount = sortCountInv(arr[:nby2])
    sortedRightArr, rightCount = sortCountInv(arr[nby2:])
    
    splitCount = 0 
    leftInd = 0
    rightInd = 0
    sortedArray = []
    for i in range(n):
        if(rightInd >= len(sortedRightArr) or \
           (leftInd < len(sortedLeftArr) and \
            sortedLeftArr[leftInd] < sortedRightArr[rightInd])):
            sortedArray.append(sortedLeftArr[leftInd])
            leftInd += 1
        else:
            sortedArray.append(sortedRightArr[rightInd])
            rightInd += 1
            if(leftInd < len(sortedLeftArr)):
                splitCount += len(sortedLeftArr) - leftInd

    totalInv = leftCount + splitCount + rightCount    
    return sortedArray, totalInv


print(sortCountInv([1, 3, 5, 2, 4, 6]))
print(sortCountInv([5, 4, 3, 2, 1]))
print(sortCountInv([1, 6, 2, 5, 4]))

# read textFile and transform it to an array
textFile = open("IntegerArray.txt", "r")
array = textFile.read().split('\n')
array = filter(None, array)
array = list(map(int, array))

sortedArray, totalInv = sortCountInv(array)
print(totalInv)