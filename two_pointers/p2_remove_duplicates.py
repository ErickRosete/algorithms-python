"""
Given an array of sorted numbers, remove all duplicate number instances from
it in-place, such that each element appears only once.
The relative order of the elements should be kept the same and 
you should not use any extra space so that that the solution 
have a space complexity of O(1).

Move all the unique elements at the beginning of the array and
after moving return the length of the subarray that has no duplicate in it.

Example 1:
Input: [2, 3, 3, 3, 6, 9, 9]
Output: 4
Explanation: The first four elements after removing the duplicates will be [2, 3, 6, 9].

Example 2:
Input: [2, 2, 2, 11]
Output: 2
Explanation: The first two elements after removing the duplicates will be [2, 11].
"""

def remove_duplicates(array=[]):
    non_dup = 1

    for i in range(len(array)):
        if array[non_dup - 1] != array[i]:
            if i != non_dup:
                array[non_dup], array[i] = array[i], array[non_dup]
            non_dup += 1
    return non_dup, array

def main():
    array = [2, 3, 3, 3, 6, 9, 9]
    output, array = remove_duplicates(array)
    print(output, array)

    array = [2, 2, 2, 11]
    output, array = remove_duplicates(array)
    print(output, array)

if __name__ == "__main__":
    main()
