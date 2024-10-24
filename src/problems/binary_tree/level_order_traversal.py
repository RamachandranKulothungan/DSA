# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []
        q = [root]
        left = 0
        right = 1
        row = -1
        row_elements = 0
        level_traversal = []
        while left < right:
            if row_elements == 0:
                row_elements = right - left
                row = row + 1
                level_traversal.append([])
            level_traversal[row].append(q[left].val)
            if q[left].left:
                q.append(q[left].left)
                right += 1
            if q[left].right:
                q.append(q[left].right)
                right += 1
            left += 1
            row_elements -= 1
        return level_traversal
