"""
Smallest Subarray with a Greater Sum (easy)

Problem Statement

Given an array of positive numbers and a positive number ‘S,’ 
find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’. 
Return 0 if no such subarray exists.

Example 1:
Input: [2, 1, 5, 2, 3, 2], S=7 
Output: 2
Explanation: The smallest subarray with a sum greater than or equal to '7' is [5, 2].

Example 2:
Input: [2, 1, 5, 2, 8], S=7 
Output: 1
Explanation: The smallest subarray with a sum greater than or equal to '7' is [8].

Example 3:
Input: [3, 4, 1, 1, 6], S=8 
Output: 3
Explanation: Smallest subarrays with a sum greater than or equal to '8' are 
[3, 4, 1] or [1, 1, 6].
"""


def min_len_subarray_sum(array=[], S: int = 1):
    for window_size in range(1, len(array)):
        window_start = 0
        window_sum = 0
        for i in range(len(array)):
            window_sum += array[i]
            if i >= window_size - 1:
                if window_sum >= S:
                    return window_size
                window_sum -= array[window_start]
                window_start += 1
    return 0


def better_min_len_subarray_sum(array=[], S: int = 1):
    window_sum = 0
    window_start = 0
    min_len = float("inf")
    for window_end in range(len(array)):
        window_sum += array[window_end]
        while window_sum >= S:
            window_size = window_end - window_start + 1
            min_len = min(window_size, min_len)
            window_sum -= array[window_start]
            window_start += 1

    if min_len == float("inf"):
        return 0
    return min_len


def main():
    print(min_len_subarray_sum(array=[2, 1, 5, 2, 3, 2], S=7))
    print(better_min_len_subarray_sum(array=[2, 1, 5, 2, 3, 2], S=7))
    print(min_len_subarray_sum(array=[2, 1, 5, 2, 8], S=7))
    print(better_min_len_subarray_sum(array=[2, 1, 5, 2, 8], S=7))
    print(min_len_subarray_sum(array=[3, 4, 1, 1, 6], S=8))
    print(better_min_len_subarray_sum(array=[3, 4, 1, 1, 6], S=8))


if __name__ == "__main__":
    main()
