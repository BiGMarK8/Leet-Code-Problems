"""
26. Remove Duplicates from Sorted Array
https://leetcode.com/problems/remove-duplicates-from-sorted-array/

Difficulty: Easy
Topics: Array, Two Pointers

Problem:
    Given an integer array nums sorted in non-decreasing order, remove the
    duplicates in-place so each unique element appears once, keeping the
    relative order. Return k, the number of unique elements. The first k
    elements of nums must hold the unique numbers in sorted order;
    anything beyond index k-1 is ignored.

Examples:
    [1,1,2]                ->  k=2, nums = [1,2,_]
    [0,0,1,1,1,2,2,3,3,4]  ->  k=5, nums = [0,1,2,3,4,_,_,_,_,_]

Constraints:
    1 <= len(nums) <= 3 * 10**4
    -100 <= nums[i] <= 100
    nums is sorted in non-decreasing order.

Approach:
    Two pointers. `k` is the write position for the next unique value; `i`
    scans the array. Because the array is sorted, duplicates sit next to
    each other, so a value is new whenever it differs from the last kept
    unique value at nums[k-1]. nums[0] is always unique, so start k at 1.

Complexity:
    Time:  O(n)  - one pass with i.
    Space: O(1)  - edits in place, no extra array.
"""


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # k is the index where the next unique number will be written.
        # nums[0] is always unique (first value), so start at 1.
        k = 1
        # i scans every element.
        for i in range(1, len(nums)):
            # nums[k-1] is the last unique number kept. The array is
            # sorted, so duplicates sit side by side; if nums[i] differs
            # from it, nums[i] is a new value.
            if nums[i] != nums[k - 1]:
                # Write the new value into the next free unique slot.
                nums[k] = nums[i]
                # Move the write position forward.
                k += 1
            # If nums[i] == nums[k-1] it's a duplicate, skip it.
        # nums[0..k-1] holds each unique value once in sorted order;
        # anything after index k-1 is leftover and ignored by the judge.
        return k


if __name__ == "__main__":
    solution = Solution()

    nums = [1, 1, 2]
    k = solution.removeDuplicates(nums)
    assert k == 2 and nums[:k] == [1, 2]

    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k = solution.removeDuplicates(nums)
    assert k == 5 and nums[:k] == [0, 1, 2, 3, 4]

    nums = [5]
    k = solution.removeDuplicates(nums)
    assert k == 1 and nums[:k] == [5]

    nums = [7, 7, 7, 7]
    k = solution.removeDuplicates(nums)
    assert k == 1 and nums[:k] == [7]

    print("All test cases passed.")
