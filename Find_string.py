"""
28. Find the Index of the First Occurrence in a String
https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

Difficulty: Easy
Topics: Two Pointers, String, String Matching

Problem:
    Given two strings needle and haystack, return the index of the first
    occurrence of needle in haystack, or -1 if needle is not part of it.

Examples:
    haystack = "sadbutsad", needle = "sad"    ->  0   (also occurs at 6)
    haystack = "leetcode",  needle = "leeto"  ->  -1

Constraints:
    1 <= len(haystack), len(needle) <= 10**4
    Both consist of only lowercase English letters.

Approach:
    Slide a window of length m over the haystack. The last valid start is
    n - m; any later start would run past the end. Compare each window's
    slice to needle and return the first index that matches, else -1.

Complexity:
    Time:  O((n - m + 1) * m)  - up to n-m+1 windows, each an m-char compare.
    Space: O(m)                - each slice copies m characters.
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)

        # The last place the needle can start is n - m; any later start
        # would run past the end of haystack.
        for i in range(n - m + 1):
            # Take m characters starting at i and compare to needle.
            if haystack[i:i + m] == needle:
                # Positions are checked left to right, so this is the first match.
                return i
        # Every start position was checked; none matched.
        return -1


if __name__ == "__main__":
    solution = Solution()
    assert solution.strStr("sadbutsad", "sad") == 0
    assert solution.strStr("leetcode", "leeto") == -1
    assert solution.strStr("a", "a") == 0
    assert solution.strStr("abc", "c") == 2
    assert solution.strStr("mississippi", "issip") == 4
    assert solution.strStr("aaa", "aaaa") == -1
    print("All test cases passed.")
