"""
20. Valid Parentheses
https://leetcode.com/problems/valid-parentheses/

Difficulty: Easy
Topics: String, Stack

Problem:
    Given a string s of just '(', ')', '{', '}', '[' and ']', determine
    if it is valid. Valid means:
      1. Open brackets are closed by the same type.
      2. Open brackets are closed in the correct order.
      3. Every closing bracket has a matching open bracket of the same type.

Examples:
    "()"      ->  True
    "()[]{}"  ->  True
    "(]"      ->  False
    "([])"    ->  True
    "([)]"    ->  False

Approach:
    Use a stack. Push every opening bracket. On a closing bracket, the
    top of the stack must be its matching open bracket, otherwise the
    string is invalid. At the end the stack must be empty, meaning every
    open bracket was closed.

Complexity:
    Time:  O(n)  - one pass over the string.
    Space: O(n)  - the stack holds up to n opening brackets.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            ')': '(',
            ']': '[',
            '}': '{',
        }  # closing bracket -> matching opening bracket
        stack = []  # holds open brackets in the order seen

        for c in s:  # scan one character at a time
            if c in pairs:  # c is a closing bracket
                # Nothing to close, or the top is the wrong type.
                if not stack or stack.pop() != pairs[c]:
                    return False
            else:  # c is an opening bracket
                stack.append(c)  # push and wait for its match

        return not stack  # valid only if every open was closed


if __name__ == "__main__":
    solution = Solution()
    assert solution.isValid("()") is True
    assert solution.isValid("()[]{}") is True
    assert solution.isValid("(]") is False
    assert solution.isValid("([])") is True
    assert solution.isValid("([)]") is False
    assert solution.isValid("(") is False
    assert solution.isValid(")") is False
    print("All test cases passed.")
