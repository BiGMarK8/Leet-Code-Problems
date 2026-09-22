"""
21. Merge Two Sorted Lists
https://leetcode.com/problems/merge-two-sorted-lists/

Difficulty: Easy
Topics: Linked List, Recursion

Problem:
    Given the heads of two sorted linked lists list1 and list2, merge them
    into one sorted list by splicing the existing nodes together, and
    return the head of the merged list.

Examples:
    [1,2,4] + [1,3,4]  ->  [1,1,2,3,4,4]
    []      + []       ->  []
    []      + [0]      ->  [0]

Approach:
    Use a dummy head so attaching the first node needs no special case.
    Keep a `tail` pointer and repeatedly splice on the smaller of the two
    current nodes, advancing that list. When one list runs out, append the
    remainder of the other (already sorted). Return dummy.next.

Complexity:
    Time:  O(n + m)  - each node from both lists is visited once.
    Space: O(1)      - nodes are relinked in place, no new nodes created.
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode()  # placeholder; makes "attach to tail" uniform
        tail = dummy        # tail points to the last node of the merged list

        while list1 and list2:  # while both lists still have nodes to compare
            if list1.val <= list2.val:  # list1's node is smaller or equal
                tail.next = list1       # splice it onto the merged list
                list1 = list1.next      # advance list1
            else:                       # list2's node is smaller
                tail.next = list2       # splice it onto the merged list
                list2 = list2.next      # advance list2
            tail = tail.next            # move tail to the node just attached

        # One list is exhausted; the other is already sorted, attach it.
        tail.next = list1 if list1 else list2

        return dummy.next  # dummy is a placeholder, skip it


# --- Local test helpers (not part of the LeetCode submission) ---
def build(values):
    dummy = ListNode()
    tail = dummy
    for v in values:
        tail.next = ListNode(v)
        tail = tail.next
    return dummy.next


def to_list(head):
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


if __name__ == "__main__":
    solution = Solution()
    assert to_list(solution.mergeTwoLists(build([1, 2, 4]), build([1, 3, 4]))) == [1, 1, 2, 3, 4, 4]
    assert to_list(solution.mergeTwoLists(build([]), build([]))) == []
    assert to_list(solution.mergeTwoLists(build([]), build([0]))) == [0]
    assert to_list(solution.mergeTwoLists(build([5]), build([1, 2, 3]))) == [1, 2, 3, 5]
    print("All test cases passed.")
