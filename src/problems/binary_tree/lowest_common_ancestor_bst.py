# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        temp = root
        while temp:
            if temp.val == p.val or temp.val == q.val:
                # print(temp.val)
                return temp
            if temp.val > p.val and temp.val > q.val:
                temp = temp.left
                continue
            if temp.val < p.val and temp.val < q.val:
                temp = temp.right
                continue
            return temp
