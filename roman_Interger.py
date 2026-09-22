"""
13. Roman to Integer
https://leetcode.com/problems/roman-to-integer/

Difficulty: Easy
Topics: Hash Table, Math, String

Problem:
    Convert a Roman numeral string to an integer. Symbols are usually
    written largest to smallest, left to right, and added together. In six
    subtractive cases a smaller symbol precedes a larger one and is
    subtracted: IV=4, IX=9, XL=40, XC=90, CD=400, CM=900.

Symbols:
    I=1, V=5, X=10, L=50, C=100, D=500, M=1000

Examples:
    "III"      ->  3
    "LVIII"    ->  58    (L=50, V=5, III=3)
    "MCMXCIV"  ->  1994  (M=1000, CM=900, XC=90, IV=4)

Approach:
    Walk through each symbol paired with the one after it. If a symbol's
    value is less than its successor's, it is subtractive, so subtract it;
    otherwise add it. The last symbol has no successor, so add its value
    at the end.

Complexity:
    Time:  O(n)  - one pass over the string.
    Space: O(1)  - the value map is fixed size.
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        # Move through pairs (a = current, b = next).
        # zip stops at the second-to-last char, so the final character
        # is never paired and is added separately below.
        for a, b in zip(s, s[1:]):
            if roman[a] < roman[b]:
                # Smaller value before a larger one means subtractive
                # notation, e.g. IV = 4, IX = 9, so subtract this digit.
                res -= roman[a]
            else:
                # Otherwise normal addition.
                res += roman[a]

        # The loop never processes the last character (no successor),
        # so add its value here.
        return res + roman[s[-1]]


if __name__ == "__main__":
    solution = Solution()
    assert solution.romanToInt("III") == 3
    assert solution.romanToInt("LVIII") == 58
    assert solution.romanToInt("MCMXCIV") == 1994
    assert solution.romanToInt("IV") == 4
    assert solution.romanToInt("IX") == 9
    assert solution.romanToInt("MMMCMXCIX") == 3999
    print("All test cases passed.")
