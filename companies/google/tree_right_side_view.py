"""
Binary Tree Right Side View

Given the root of a binary trees, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example 1:
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
Explanation:

Example 2:
Input: root = [1,2,3,4,null,null,null,5]
Output: [1,3,4,5]
Explanation:

Example 3:
Input: root = [1,null,3]
Output: [1,3]

Example 4:
Input: root = []
Output: []


Constraints:
The number of nodes in the trees is in the range [0, 100].
-100 <= Node.val <= 100
"""

from collections import deque
from typing import Optional, List


# Definition for a binary trees node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        # if root is empty
        if not root:
            return []

        queue = deque()
        queue.append(root)
        next_row = []
        result = []

        while queue:
            elem = queue.popleft()

            if elem.left:
                next_row.append(elem.left)
            if elem.right:
                next_row.append(elem.right)

            if not queue:
                result.append(elem.val)
                queue.extend(next_row)
                next_row = []

        return result
