"""
Reverse Linked List
------------

Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
------------
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
------------
Input: head = [1,2]
Output: [2,1]

Example 3:
------------
Input: head = []
Output: []


Constraints:
------------
The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous_node = None
        current_node = head

        # We iterate until current_node becomes None
        while(current_node is not None):

            # Store the next node before reversing
            next_node = current_node.next

            # Reverse the current node's pointer
            # This is the core reversal step
            current_node.next = previous_node

            # Move pointers one position ahead
            previous_node = current_node
            current_node = next_node

        # previous_node is now the head of reversed list
        return previous_node
