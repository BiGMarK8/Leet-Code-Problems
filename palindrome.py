"""
9. Palindrome Number
https://leetcode.com/problems/palindrome-number/

Difficulty: Easy
Topics: Math

Problem:
    Given an integer `x`, return `true` if `x` is a palindrome, and
    `false` otherwise. A palindrome reads the same forwards and backwards.

Examples:
    x = 121   ->  True   (121 reversed is 121)
    x = -121  ->  False  (the '-' sign breaks front/back symmetry)
    x = 10    ->  False  (reversed it reads "01")

Constraints:
    -2**31 <= x <= 2**31 - 1

Approach:
    Negative numbers can never be palindromes because the '-' sign only
    appears at the front. For non-negatives, compare the string form of x
    to its reverse.

Complexity:
    Time:  O(d)  - d is the number of digits (work is proportional to len(str(x))).
    Space: O(d)  - the string and its reverse.
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers can never be palindromes: the '-' sign
        # only appears at the front, breaking front/back symmetry.
        if x < 0:
            return False

        s = str(x)
        # Compare the string to its reverse to check for symmetry.
        return s == s[::-1]


if __name__ == "__main__":
    solution = Solution()
    assert solution.isPalindrome(121) is True
    assert solution.isPalindrome(-121) is False
    assert solution.isPalindrome(10) is False
    assert solution.isPalindrome(0) is True
    print("All test cases passed.")
