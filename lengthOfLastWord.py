"""
58. Length of Last Word
https://leetcode.com/problems/length-of-last-word/

Difficulty: Easy
Topics: String

Problem:
    Given a string s of words and spaces, return the length of the last
    word. A word is a maximal run of non-space characters.

Examples:
    "Hello World"                  ->  5  (last word "World")
    "   fly me   to   the moon  "  ->  4  (last word "moon")
    "luffy is still joyboy"        ->  6  (last word "joyboy")

Constraints:
    1 <= len(s) <= 10**4
    s consists of only English letters and spaces.
    There is at least one word in s.

Approach:
    Scan from the end. First skip any trailing spaces, then count
    characters backwards until hitting a space or the start of the string.
    That run is the last word.

Complexity:
    Time:  O(n)  - a single backward scan in the worst case.
    Space: O(1)  - only an index and a counter.
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Start at the last character of the string.
        i = len(s) - 1

        # Skip trailing spaces.
        while i >= 0 and s[i] == ' ':
            i -= 1

        # Count letters backwards until a space or the start of the
        # string; those letters are the last word.
        length = 0
        while i >= 0 and s[i] != ' ':
            length += 1
            i -= 1

        return length


if __name__ == "__main__":
    solution = Solution()
    assert solution.lengthOfLastWord("Hello World") == 5
    assert solution.lengthOfLastWord("   fly me   to   the moon  ") == 4
    assert solution.lengthOfLastWord("luffy is still joyboy") == 6
    assert solution.lengthOfLastWord("a") == 1
    assert solution.lengthOfLastWord("day ") == 3
    print("All test cases passed.")
