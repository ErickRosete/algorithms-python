"""
Given an array, find the average of each subarray of ‘K’ contiguous elements in it.

Example
input: [1, 3, 2, 6, -1, 4, 1, 8, 2], K=5
Output: [2.2, 2.8, 2.4, 3.6, 2.8]
"""


def subarray_average(array=[], k: int = 1):
    if len(array) < k:
        return False

    av_array = []
    acum = 0
    for i in range(len(array)):
        acum += array[i]
        if i >= k - 1:
            av_array.append(acum / k)
            acum -= array[i - k + 1]
    return av_array


def main():
    array = [1, 3, 2, 6, -1, 4, 1, 8, 2]
    output = subarray_average(array, k=5)
    print(output)


if __name__ == "__main__":
    main()
