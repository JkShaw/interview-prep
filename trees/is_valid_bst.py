"""
Validate Binary Search Tree

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys strictly less than the node's key.
The right subtree of a node contains only nodes with keys strictly greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Example 1:
Input: root = [2,1,3]
Output: true

Example 2:
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.


Constraints:
The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1
"""
from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        queue = deque([(root, float('-inf'), float('inf'))])

        while queue:
            node, l, r = queue.popleft()

            if not (l < node.val < r):
                return False

            if node.left:
                queue.append((node.left, l, node.val))
            if node.right:
                queue.append((node.right, node.val, r))

        return True

    def isValidBSTRecursive(self, root: Optional[TreeNode]) -> bool:
        def helper(node, left_max, right_max):
            if not node:
                return True

            if left_max < node.val < right_max:
                return helper(node.left, left_max, node.val) and helper(node.right, node.val, right_max)
            else:
                return False

        return helper(root, float('-inf'), float('inf'))
