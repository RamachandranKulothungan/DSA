class Solution:
    def dfs(self, node):
        left_dfs = 0
        right_dfs = 0
        if node.left:
            left_dfs = self.dfs(node.left)
        if node.right:
            right_dfs = self.dfs(node.right)
        return 1 + max(left_dfs, right_dfs)

    def maxDepth(self, root):
        if root:
            return self.dfs(root)
        return 0
