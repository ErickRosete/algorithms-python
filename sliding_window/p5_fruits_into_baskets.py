"""
You are visiting a farm to collect fruits. The farm has a single row of fruit trees. 
You will be given two baskets, and your goal is to pick as many fruits as possible to be placed in the given baskets.

You will be given an array of characters where each character represents a fruit tree. 
The farm has following restrictions:

Each basket can have only one type of fruit. There is no limit to how many fruit a basket can hold.
You can start with any tree, but you can’t skip a tree once you have started.
You will pick exactly one fruit from every tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.
Write a function to return the maximum number of fruits in both baskets.


Example 1:
Input: Fruit=['A', 'B', 'C', 'A', 'C']
Output: 3
Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']

Example 2:
Input: Fruit = ['A', 'B', 'C', 'B', 'B', 'C']
Output: 5
Explanation: We can put 3 'B' in one basket and two 'C' in the other basket. This can be done if we start with the second letter: ['B', 'C', 'B', 'B', 'C']
"""


def fruits_into_baskets(fruit_list=[]):
    fruit_frequency = {}
    window_start = 0
    max_len = -float("inf")

    for window_end in range(len(fruit_list)):
        right_fruit = fruit_list[window_end]
        if right_fruit not in fruit_frequency:
            fruit_frequency[right_fruit] = 0
        fruit_frequency[right_fruit] += 1

        while len(fruit_frequency) > 2:
            left_fruit = fruit_list[window_start]
            fruit_frequency[left_fruit] -= 1
            if fruit_frequency[left_fruit] == 0:
                del fruit_frequency[left_fruit]
            window_start += 1

        max_len = max(max_len, window_end - window_start + 1)

    return max_len


def main():
    print(fruits_into_baskets(fruit_list=["A", "B", "C", "A", "C"]))
    print(fruits_into_baskets(fruit_list=["A", "B", "C", "B", "B", "C"]))


if __name__ == "__main__":
    main()
