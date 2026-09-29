"""
35. Search Insert Position
https://leetcode.com/problems/search-insert-position/

Difficulty: Easy
Topics: Array, Binary Search

Problem:
    Given a sorted array of distinct integers and a target, return the
    index of target if found. If not, return the index where it would be
    inserted to keep the array sorted. Must run in O(log n).

Examples:
    nums = [1,3,5,6], target = 5  ->  2
    nums = [1,3,5,6], target = 2  ->  1
    nums = [1,3,5,6], target = 7  ->  4

Constraints:
    1 <= len(nums) <= 10**4
    -10**4 <= nums[i], target <= 10**4
    nums contains distinct values sorted in ascending order.

Approach:
    Binary search over the inclusive range [left, right]. If nums[mid] is
    the target, return mid. If it's too small, discard mid and everything
    left of it; if too big, discard mid and everything right. When the
    loop ends, left has landed on the first index whose value exceeds
    target, which is exactly the insert position.

Complexity:
    Time:  O(log n)  - halves the range each step.
    Space: O(1)      - only pointers.
"""


class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        # Search range is nums[left .. right] with both ends included.
        left, right = 0, len(nums) - 1

        # While the range still has at least one element.
        while left <= right:
            # Index of the middle element of the current range.
            mid = (left + right) // 2

            if nums[mid] == target:
                # Found, return the index.
                return mid
            elif nums[mid] < target:
                # Middle is too small, so target must be to the right;
                # throw away mid and everything to its left.
                left = mid + 1
            else:
                # Middle is too big, so target must be to the left;
                # throw away mid and everything to its right.
                right = mid - 1

        # Not found: the loop ends with left == right + 1, and left is now
        # the first index whose value is bigger than target, which is
        # where target would be inserted.
        return left


if __name__ == "__main__":
    solution = Solution()
    assert solution.searchInsert([1, 3, 5, 6], 5) == 2
    assert solution.searchInsert([1, 3, 5, 6], 2) == 1
    assert solution.searchInsert([1, 3, 5, 6], 7) == 4
    assert solution.searchInsert([1, 3, 5, 6], 0) == 0
    assert solution.searchInsert([1], 0) == 0
    assert solution.searchInsert([1], 2) == 1
    print("All test cases passed.")
