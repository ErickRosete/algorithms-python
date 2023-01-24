"""
Given a string, find the length of the longest substring, which has all distinct characters.

Example 1:
Input: String="aabccbb"
Output: 3
Explanation: The longest substring with distinct characters is "abc".

Example 2:
Input: String="abbbb"
Output: 2
Explanation: The longest substring with distinct characters is "ab".

Example 3:
Input: String="abccde"
Output: 3
Explanation: Longest substrings with distinct characters are "abc" & "cde".
"""


def non_repeat_substring(str1=""):
    """Better use of the dict to store position instead of frequency, helps avoid inner while"""
    last_seen_char_idx = {}
    window_start = 0
    max_len = -float("inf")

    for window_end in range(len(str1)):
        right_char = str1[window_end]
        if right_char in last_seen_char_idx:
            window_start = max(window_start, last_seen_char_idx[right_char] + 1)
        last_seen_char_idx[right_char] = window_end
        max_len = max(max_len, window_end - window_start + 1)
    return max_len


def get_len_long_subst_dist_char(str1=""):
    char_frequency = {}
    window_start = 0
    max_len = -float("inf")

    for window_end in range(len(str1)):
        right_char = str1[window_end]
        if right_char not in char_frequency:
            char_frequency[right_char] = 0
        char_frequency[right_char] += 1

        while char_frequency[right_char] > 1:
            left_char = str1[window_start]
            char_frequency[left_char] -= 1
            window_start += 1

        max_len = max(max_len, window_end - window_start + 1)

    return max_len


def main():
    print(get_len_long_subst_dist_char(str1="aabccbb"))
    print(non_repeat_substring(str1="aabccbb"))
    print(get_len_long_subst_dist_char(str1="abbbb"))
    print(non_repeat_substring(str1="abbbb"))
    print(get_len_long_subst_dist_char(str1="abccde"))
    print(non_repeat_substring(str1="abccde"))


if __name__ == "__main__":
    main()
