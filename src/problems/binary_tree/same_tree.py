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
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
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
