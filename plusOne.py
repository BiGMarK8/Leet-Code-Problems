"""
66. Plus One
https://leetcode.com/problems/plus-one/

Difficulty: Easy
Topics: Array, Math

Problem:
    A large integer is given as an array of digits, most significant
    first, with no leading zeros. Increment it by one and return the
    resulting array of digits.

Examples:
    [1,2,3]    ->  [1,2,4]
    [4,3,2,1]  ->  [4,3,2,2]
    [9]        ->  [1,0]

Constraints:
    1 <= len(digits) <= 100
    0 <= digits[i] <= 9
    No leading zeros.

Approach:
    Walk from the last digit (ones place) to the first. If a digit is less
    than 9, adding one causes no carry: increment it and return. If it is
    9, it becomes 0 and the carry moves left to the next digit. If every
    digit was 9, the loop ends with a carry still pending, so prepend 1
    (e.g. [9,9] -> [1,0,0]).

Complexity:
    Time:  O(n)  - one backward pass.
    Space: O(1)  - in place, except the all-nines case that prepends a digit.
"""


class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        # Go from the last digit (ones place) to the first.
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                # No carry needed: add 1 to this digit and stop.
                digits[i] += 1
                return digits
            # The digit is 9, so 9 + 1 = 10: write 0 and carry 1 to the
            # next digit on the left (handled in the next loop iteration).
            digits[i] = 0
        # The loop finishes only if every digit was 9 ([9,9] -> [0,0]).
        # The carry is still left over, so put a 1 at the front ([1,0,0]).
        return [1] + digits


if __name__ == "__main__":
    solution = Solution()
    assert solution.plusOne([1, 2, 3]) == [1, 2, 4]
    assert solution.plusOne([4, 3, 2, 1]) == [4, 3, 2, 2]
    assert solution.plusOne([9]) == [1, 0]
    assert solution.plusOne([9, 9]) == [1, 0, 0]
    assert solution.plusOne([1, 9, 9]) == [2, 0, 0]
    assert solution.plusOne([0]) == [1]
    print("All test cases passed.")
