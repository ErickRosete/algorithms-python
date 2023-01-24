"""Given a string, find the length of the longest substring in it with no more than K distinct characters.

You can assume that K is less than or equal to the length of the given string.

Example 1:

Input: String="araaci", K=2
Output: 4
Explanation: The longest substring with no more than '2' distinct characters is "araa".
Example 2:

Input: String="araaci", K=1
Output: 2
Explanation: The longest substring with no more than '1' distinct characters is "aa".

Input: String="cbbebi", K=3
Output: 5
Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi".
"""


def longest_substring_distinct_characters(input_string=[], K: int = 1):
    window_chars = {}
    window_start = 0
    max_len = -float("inf")

    for window_end in range(len(input_string)):
        cur_char = input_string[window_end]
        if cur_char not in window_chars:
            window_chars[cur_char] = 0
        window_chars[cur_char] += 1

        while len(window_chars) > K:
            del_char = input_string[window_start]
            window_chars[del_char] -= 1
            if window_chars[del_char] == 0:
                del window_chars[del_char]
            window_start += 1

        max_len = max(max_len, window_end - window_start + 1)

    return max_len


def main():
    print(longest_substring_distinct_characters(input_string="araaci", K=2))
    print(longest_substring_distinct_characters(input_string="araaci", K=1))
    print(longest_substring_distinct_characters(input_string="cbbebi", K=3))


if __name__ == "__main__":
    main()
