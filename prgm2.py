# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 13:57:59 2023

@author: Aishwarya V B
"""


def majority_elements(nums):
    if not nums:
        return []

    candidate1, candidate2 = 0, 0
    count1, count2 = 0, 0

    # Voting phase
    for num in nums:
        if num == candidate1:
            count1 += 1
        elif num == candidate2:
            count2 += 1
        elif count1 == 0:
            candidate1 = num
            count1 = 1
        elif count2 == 0:
            candidate2 = num
            count2 = 1
        else:
            count1 -= 1
            count2 -= 1

    # Count occurrences of candidates
    count1 = count2 = 0
    for num in nums:
        if num == candidate1:
            count1 += 1
        elif num == candidate2:
            count2 += 1

    # Check if candidates appear more than ⌊ n/3 ⌋ times
    result = []
    if count1 > len(nums) // 3:
        result.append(candidate1)
    if count2 > len(nums) // 3 and candidate1 != candidate2:
        result.append(candidate2)

    return result

# Example 1
nums1 = [3, 2, 3]
output1 = majority_elements(nums1)
print(f"Example 1 Output: {output1}")

# Example 2
nums2 = [1]
output2 = majority_elements(nums2)
print(f"Example 2 Output: {output2}")

# Example 3
nums3 = [1, 2]
output3 = majority_elements(nums3)
print(f"Example 3 Output: {output3}")
