"""
Given an array of positive numbers and a positive number ‘k,’ find the maximum sum of any
contiguous subarray of size ‘k’.

Example 1
Input: [2, 1, 5, 1, 3, 2], k=3 
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3].

Example 2
Input: [2, 3, 4, 1, 5], k=2 
Output: 7
Explanation: Subarray with maximum sum is [3, 4].
"""


def subarray_max(array=[], k: int = 1):
    if len(array) < k:
        return False

    acum = 0
    max_val = -float("inf")
    for i in range(len(array)):
        acum += array[i]
        if i >= k - 1:
            max_val = max(acum, max_val)
            acum -= array[i - k + 1]
    return max_val


def main():
    array = [2, 1, 5, 1, 3, 2]
    output_one = subarray_max(array, k=3)
    print(output_one)
    array = [2, 3, 4, 1, 5]
    output_two = subarray_max(array, k=2)
    print(output_two)


if __name__ == "__main__":
    main()
