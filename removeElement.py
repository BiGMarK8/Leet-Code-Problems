"""
27. Remove Element
https://leetcode.com/problems/remove-element/

Difficulty: Easy
Topics: Array, Two Pointers

Problem:
    Given an integer array nums and an integer val, remove all occurrences
    of val in-place. The order of the remaining elements may change.
    Return k, the number of elements not equal to val, with those first k
    elements of nums holding the kept values. Anything beyond index k-1
    does not matter.

Examples:
    nums = [3,2,2,3],           val = 3  ->  k=2, nums = [2,2,_,_]
    nums = [0,1,2,2,3,0,4,2],   val = 2  ->  k=5, first 5 are the non-2 values

Constraints:
    0 <= len(nums) <= 100
    0 <= nums[i] <= 50
    0 <= val <= 100

Approach:
    Two pointers. `index` is the write position for the next kept value
    and also counts how many have been kept. `i` scans every element; when
    nums[i] is not val, copy it to nums[index] and advance index. Values
    equal to val are simply skipped and later overwritten.

Complexity:
    Time:  O(n)  - one pass with i.
    Space: O(1)  - edits in place, no extra array.
"""


class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        # index = where the next kept number will be written,
        # and also counts how many numbers have been kept.
        index = 0
        # i visits every element in the array.
        for i in range(len(nums)):
            # Keep only numbers not equal to val.
            if nums[i] != val:
                # Copy the kept number into the next free slot at the front.
                nums[index] = nums[i]
                # Move the write position forward one.
                index += 1
            # If nums[i] == val, do nothing; it gets skipped and a later
            # kept number will overwrite its spot.

        # nums[0..index-1] now holds every number that isn't val;
        # anything after index-1 is ignored. index is the count (k).
        return index


if __name__ == "__main__":
    solution = Solution()

    nums = [3, 2, 2, 3]
    k = solution.removeElement(nums, 3)
    assert k == 2 and sorted(nums[:k]) == [2, 2]

    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    k = solution.removeElement(nums, 2)
    assert k == 5 and sorted(nums[:k]) == [0, 0, 1, 3, 4]

    nums = []
    k = solution.removeElement(nums, 1)
    assert k == 0

    nums = [1, 1, 1]
    k = solution.removeElement(nums, 1)
    assert k == 0

    nums = [4, 5]
    k = solution.removeElement(nums, 9)
    assert k == 2 and sorted(nums[:k]) == [4, 5]

    print("All test cases passed.")
