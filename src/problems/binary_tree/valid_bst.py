# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValid(self, root, max_value, min_value):
        valid_left = True
        valid_right = True
        if root.left:
            if root.left.val >= root.val:
                return False
            if root.left.val <= min_value:
                return False
            valid_left = self.isValid(root.left, root.val, min_value)
        if not valid_left:
            return False
        if root.right:
            if root.right.val <= root.val:
                return False
            if root.right.val >= max_value:
                return False
            valid_right = self.isValid(root.right, max_value, root.val)
        if not valid_right:
            return False
        return True

    def isValidBST(self, root):
        return self.isValid(root, float("inf"), -float("inf"))
