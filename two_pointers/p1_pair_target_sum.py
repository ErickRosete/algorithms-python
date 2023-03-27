"""
Given an array of sorted numbers and a target sum, 
find a pair in the array whose sum is equal to the given target.

Example
Input: [1, 2, 3, 4, 6], target=6
Output: [1, 3]
Explanation: The numbers at index 1 and 3 add up to 6: 2+4=6

Input: [2, 5, 9, 11], target=11
Output: [0, 2]
Explanation: The numbers at index 0 and 2 add up to 11: 2+9=11

"""


def pair_target_sum(array=[], target: float = 0):
    left_pos, right_pos = 0, len(array) - 1
    while (left_pos < right_pos):
        pos_sum = array[left_pos] + array[right_pos]
        if pos_sum == target:
            return [left_pos, right_pos]
        elif pos_sum > target:
            right_pos -= 1
        else:
            left_pos += 1
    return [-1, -1]

def pair_with_targetsum(arr, target_sum):
  nums = {}  # to store numbers and their indices
  for i, num in enumerate(arr):
    if target_sum - num in nums:
      return [nums[target_sum - num], i]
    else:
      nums[arr[i]] = i
  return [-1, -1]


def main():
    array = [1, 2, 3, 4, 6]
    output = pair_target_sum(array, target=6)
    print(output)


if __name__ == "__main__":
    main()
