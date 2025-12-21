"""
Remove Nth Node From End of List

Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]


Constraints:
The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
"""

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        leading_pointer = head
        trailing_pointer = head

        # Advance the leading pointer by n steps
        for _ in range(n):
            if not leading_pointer:
                return head
            leading_pointer = leading_pointer.next

        # If leading pointer reaches the end first, remove the head
        if not leading_pointer:
            return head.next

        # Advance both pointers until leading pointer reaches the end.
        while leading_pointer.next:
            leading_pointer = leading_pointer.next
            trailing_pointer = trailing_pointer.next

        # trailing pointer is now one node before the one to remove
        trailing_pointer.next = trailing_pointer.next.next

        return head