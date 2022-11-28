"""Problem 26. Remove Duplicates from Sorted Array
"""

from typing import List


def solution(nums: List[int]) -> int:
    prev = None
    last_index = 0
    count = 0
    for index, num in enumerate(nums):
        if num == prev:
            continue
        if index != last_index:
            nums[last_index + 1] = num
            last_index += 1
        else:
            last_index = index
        prev = num
        count += 1
    return count
