# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root
        queue = [root]
        start=0
        end = 0
        while start<=end:
            temp = queue[start].left
            queue[start].left = queue[start].right
            queue[start].right = temp
            if queue[start].left: 
                queue.append(queue[start].left)
                end = end + 1
            if queue[start].right: 
                queue.append(queue[start].right)
                end = end + 1
            start = start + 1
        return root
        