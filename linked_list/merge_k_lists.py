import heapq
from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Min-heap (list) to store elements as (value, index, ListNode)
        # The 'index' helps break ties if two nodes have the same value,
        # preventing errors when Python compares ListNode objects directly.
        min_heap = []

        # Create a dummy head for the merged list
        dummy = ListNode(0)
        current = dummy

        # Initialize the heap with the head of each linked list
        for i, head in enumerate(lists):
            if head:
                # We use a unique counter 'i' to handle tie-breaking among nodes with same value
                heapq.heappush(min_heap, (head.val, i, head))

        while min_heap:
            # Pop the smallest node from the heap
            val, i, node = heapq.heappop(min_heap)

            # Attach the popped node to the merged list
            current.next = node
            current = current.next

            # If the popped node has a next node, push the next node onto the heap
            if node.next:
                # We must use a unique index again to handle tie-breaking
                # We reuse the previous list index 'i' as the tie-breaker since it is unique per list stream
                heapq.heappush(min_heap, (node.next.val, i, node.next))

        return dummy.next