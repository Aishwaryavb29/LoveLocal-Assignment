# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 13:53:33 2023

@author: Aishwarya V B
"""


def length_of_last_word(s):
    # Split the string into words
    words = s.split()

    # Check if there are any words in the string
    if not words:
        return 0

    # Return the length of the last word
    return len(words[-1])

# Example 1
input_str1 = "Hello World"
output1 = length_of_last_word(input_str1)
print(f"Example 1 Output: {output1}")

# Example 2
input_str2 = "   fly me   to   the moon  "
output2 = length_of_last_word(input_str2)
print(f"Example 2 Output: {output2}")

# Example 3
input_str3 = "luffy is still joyboy"
output3 = length_of_last_word(input_str3)
print(f"Example 3 Output: {output3}")
