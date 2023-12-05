# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 13:59:44 2023

@author: Aishwarya V B
"""


def count_digit_one(n):
    count = 0
    factor = 1

    while factor <= n:
        divider = factor * 10
        count += (n // divider) * factor + min(max(n % divider - factor + 1, 0), factor)
        factor *= 10

    return count

# Example 1
input1 = 13
output1 = count_digit_one(input1)
print(f"Example 1 Output: {output1}")

# Example 2
input2 = 0
output2 = count_digit_one(input2)
print(f"Example 2 Output: {output2}")
