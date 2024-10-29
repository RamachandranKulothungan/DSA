"""
Kth Smallest Integer in BST
Solved 
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) in the tree.

A binary search tree satisfies the following constraints:

The left subtree of every node contains only nodes with keys less than the node's key.
The right subtree of every node contains only nodes with keys greater than the node's key.
Both the left and right subtrees are also binary search trees.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def count(self, root):
        left_count = 0
        if root.left:
            left_count = self.count(root.left)
        right_count = 0
        if root.right:
            right_count = self.count(root.right)
        return right_count + left_count + 1

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        left_count = 0
        if root.left:
            left_count = self.count(root.left)
        right_count = 0
        if root.right:
            right_count = self.count(root.right)
        if k < left_count + 1:
            return self.kthSmallest(root.left, k)
        if k == left_count + 1:
            return root.val
        if k > left_count + 1:
            return self.kthSmallest(root.right, k - left_count - 1)
