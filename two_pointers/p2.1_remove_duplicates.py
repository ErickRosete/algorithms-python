"""
Problem 1: Given an unsorted array of numbers and a target ‘key’, 
remove all instances of ‘key’ in-place and return the new length of the array.

Example 1:
Input: [3, 2, 3, 6, 3, 10, 9, 3], Key=3
Output: 4
Explanation: The first four elements after removing every 'Key' will be [2, 6, 10, 9].

Example 2:
Input: [2, 11, 2, 2, 1], Key=2
Output: 2
Explanation: The first two elements after removing every 'Key' will be [11, 1].
"""

def remove_duplicates(array=[], key: float = 3):
    curr = 0

    i = 0
    for i in range(len(array)):
        if array[i] != key:
            if i != curr:
                array[curr], array[i] = array[i], array[curr]
            curr += 1
    return curr, array

def main():
    array = [2, 3, 3, 3, 6, 9, 9]
    output, array = remove_duplicates(array, key=3)
    print(output, array)

    array = [2, 11, 2, 2, 1]
    output, array = remove_duplicates(array, key=2)
    print(output, array)

if __name__ == "__main__":
    main()
