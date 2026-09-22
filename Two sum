"""
1. Two Sum
https://leetcode.com/problems/two-sum/

Difficulty: Easy
Topics: Array, Hash Table

Problem:
    Given an array of integers `nums` and an integer `target`, return the
    indices of the two numbers such that they add up to `target`.

    Each input has exactly one solution, and the same element may not be
    used twice. The answer can be returned in any order.

Examples:
    nums = [2, 7, 11, 15], target = 9  ->  [0, 1]   (nums[0] + nums[1] == 9)
    nums = [3, 2, 4],       target = 6  ->  [1, 2]
    nums = [3, 3],          target = 6  ->  [0, 1]

Approach:
    Single pass with a hash map. For each number, check whether its
    complement (target - num) has already been seen. If so, return the
    stored index and the current index. Otherwise, store the number and
    its index and continue.

Complexity:
    Time:  O(n)  - one pass over the array, O(1) average map lookups.
    Space: O(n)  - up to n entries stored in the map.
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i
        return []


if __name__ == "__main__":
    solution = Solution()
    assert solution.twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert solution.twoSum([3, 2, 4], 6) == [1, 2]
    assert solution.twoSum([3, 3], 6) == [0, 1]
    print("All test cases passed.")
