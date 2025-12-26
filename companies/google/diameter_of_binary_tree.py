"""
Diameter of Binary Tree

Given the root of a binary trees, return the length of the diameter of the trees.
The diameter of a binary trees is the length of the longest path between any two nodes in a trees. This path may or may not pass through the root.
The length of a path between two nodes is represented by the number of edges between them.


Example 1:
Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

Example 2:
Input: root = [1,2]
Output: 1


Constraints:
The number of nodes in the trees is in the range [1, 104].
-100 <= Node.val <= 100
"""

from typing import Optional

# Definition for a binary trees node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        # helper function to get height at node
        def height(node):
            # node is null
            if not node:
                return 0

            left_height = height(node.left)
            right_height = height(node.right)

            self.diameter = max(self.diameter, left_height + right_height)
            return 1 + max(left_height, right_height)

        height(root)
        return self.diameter


"""
Time Complexity: 
O(n) 

Space Complexity:
O(n)          
"""
