"""
14. Longest Common Prefix
https://leetcode.com/problems/longest-common-prefix/

Difficulty: Easy
Topics: String, Trie

Problem:
    Find the longest common prefix string among an array of strings.
    Return "" if there is no common prefix.

Examples:
    ["flower", "flow", "flight"]  ->  "fl"
    ["dog", "racecar", "car"]     ->  ""

Constraints:
    1 <= len(strs) <= 200
    0 <= len(strs[i]) <= 200
    strs[i] consists of lowercase English letters if non-empty.

Approach:
    Sort the list lexicographically. After sorting, only the first and
    last strings can differ the most, so the common prefix of the whole
    list equals the common prefix of just those two. Compare them
    character by character up to the shorter length.

Complexity:
    Time:  O(n log n * m)  - sorting n strings that compare up to m chars.
    Space: O(1)            - ignoring the output and sort overhead.
"""


class Solution:
    def longestCommonPrefix(self, v: list[str]) -> str:
        ans = ""            # accumulates the common prefix
        v = sorted(v)       # sort lexicographically
        first = v[0]
        last = v[-1]

        # Iterate up to the length of the shorter of the two extremes.
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                # Mismatch: everything before i is the common prefix.
                return ans
            ans += first[i]
        return ans


if __name__ == "__main__":
    solution = Solution()
    assert solution.longestCommonPrefix(["flower", "flow", "flight"]) == "fl"
    assert solution.longestCommonPrefix(["dog", "racecar", "car"]) == ""
    assert solution.longestCommonPrefix(["a"]) == "a"
    assert solution.longestCommonPrefix(["", "abc"]) == ""
    assert solution.longestCommonPrefix(["abc", "abc"]) == "abc"
    print("All test cases passed.")
