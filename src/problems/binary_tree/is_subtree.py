# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def compare_nodes(self, node1, node2):
        if (node1 is None) and (node2 is None):
            return True
        if (node1 is None) or (node2 is None):
            return False
        if node1.val == node2.val:
            return True
        return False

    def isSameTree(self, p, q):
        q1 = [p]
        q2 = [q]
        while q1 and q2:
            curr1 = q1.pop(0)
            curr2 = q2.pop(0)
            if not self.compare_nodes(curr1, curr2):
                return False
            if not curr1 and not curr2:
                continue
            if not self.compare_nodes(curr1.left, curr2.left):
                return False
            q1.append(curr1.left)
            q2.append(curr2.left)
            if not self.compare_nodes(curr1.right, curr2.right):
                return False
            q1.append(curr1.right)
            q2.append(curr2.right)
        return True

    def isSubtree(self, root, subRoot):
        q = [root]
        while q:
            curr = q.pop(0)
            if self.isSameTree(curr, subRoot):
                return True
            if curr:
                q.append(curr.left)
                q.append(curr.right)
        return False
