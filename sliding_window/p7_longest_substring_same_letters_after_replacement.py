"""
Given a string with lowercase letters only, if you are allowed to replace no more than ‘k’ letters 
with any letter, find the length of the longest substring having the same letters after replacement.

Example 1:
Input: String="aabccbb", k=2
Output: 5
Explanation: Replace the two 'c' with 'b' to have a longest repeating substring "bbbbb".

Example 2:
Input: String="abbcb", k=1
Output: 4
Explanation: Replace the 'c' with 'b' to have a longest repeating substring "bbbb".

Example 3:
Input: String="abccde", k=1
Output: 3
Explanation: Replace the 'b' or 'd' with 'c' to have the longest repeating substring "ccc".

"""


def longest_substring_after_replacement(str1="", k=1):
    """We store a hashmap with the required replacements to only leave that character"""
    req_rep = {}  # Required replacements
    window_start = 0
    max_len = -float("inf")

    for window_end in range(len(str1)):
        right_char = str1[window_end]
        if right_char not in req_rep:
            req_rep[right_char] = window_end - window_start

        min_rep = float("inf")
        for char in req_rep.keys():
            if char != right_char:
                req_rep[char] += 1
            min_rep = min(min_rep, req_rep[char])

        while min_rep > k:
            left_char = str1[window_start]
            for char in req_rep.keys():
                if char != left_char:
                    req_rep[char] -= 1
                min_rep = min(min_rep, req_rep[char])
            window_start += 1

        max_len = max(max_len, window_end - window_start + 1)
    return max_len


def len_of_longest_substring(str1="", k=1):
    """We store a hashmap with the frequency of each character"""
    char_frequency = {}
    window_start = 0
    max_len = -float("inf")

    for window_end in range(len(str1)):
        right_char = str1[window_end]
        if right_char not in char_frequency:
            char_frequency[right_char] = 0
        char_frequency[right_char] += 1

        #  max(char_frequency.values()) is the most frequent char frequency
        while (window_end - window_start + 1) - max(char_frequency.values()) > k:
            left_char = str1[window_start]
            char_frequency[left_char] -= 1
            window_start += 1

        max_len = max(max_len, window_end - window_start + 1)
    return max_len

def optim_len_of_longest_substring(str1="", k=1):
    """
    We store a hashmap with the frequency of each character, taking away the inner while
    by tracking the frequency of the most frequent character
    """
    char_frequency = {}
    window_start = 0
    max_len = -float("inf")
    most_freq = 0

    for window_end in range(len(str1)):
        right_char = str1[window_end]
        if right_char not in char_frequency:
            char_frequency[right_char] = 0
        char_frequency[right_char] += 1

        most_freq = max(char_frequency[right_char], most_freq)

        if (window_end - window_start + 1) - most_freq > k:
            left_char = str1[window_start]
            char_frequency[left_char] -= 1
            window_start += 1

        max_len = max(max_len, window_end - window_start + 1)
    return max_len


def main():
    print(longest_substring_after_replacement(str1="aabccbb", k=2))
    print(len_of_longest_substring(str1="aabccbb", k=2))
    print(optim_len_of_longest_substring(str1="aabccbb", k=2))

    print(longest_substring_after_replacement(str1="abbcb", k=1))
    print(len_of_longest_substring(str1="abbcb", k=1))
    print(optim_len_of_longest_substring(str1="abbcb", k=1))

    print(longest_substring_after_replacement(str1="abccde", k=1))
    print(len_of_longest_substring(str1="abccde", k=1))
    print(optim_len_of_longest_substring(str1="abccde", k=1))


if __name__ == "__main__":
    main()
