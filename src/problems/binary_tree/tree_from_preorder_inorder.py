# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTreeRec(self, p_l, p_r, i_l, i_r):
        if p_r == p_l:
            return None
        if p_r - p_l == 1:
            return TreeNode(self.preorder[p_l])
        root = self.preorder[p_l]
        index = self.inorder.index(root)
        length = index - i_l
        # print(preorder[p_l: p_r], inorder[i_l: i_r], root, index)
        root_tree = self.buildTreeRec(p_l, p_l + 1, i_l + length, i_l + length + 1)
        root_left_tree = self.buildTreeRec(p_l + 1, p_l + 1 + length, i_l, i_l + length)
        root_right_tree = self.buildTreeRec(
            p_l + 1 + length, p_r, i_l + length + 1, i_r
        )
        root_tree.left = root_left_tree
        root_tree.right = root_right_tree
        return root_tree

    def buildTree(self, preorder, inorder):
        self.preorder = preorder
        self.inorder = inorder
        return self.buildTreeRec(0, len(preorder), 0, len(inorder))


Solution().buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])


"""
Less optimum: passing copy of list for each recursice call
"""
# class Solution:
#     def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
#         if not preorder:
#             return None
#         if len(preorder)==1:
#             return TreeNode(preorder[0])
#         root = preorder[0]
#         index = inorder.index(root)
#         root_tree = self.buildTree(preorder[0:1], inorder[index:index+1])
#         root_left_tree = self.buildTree(preorder[1:1+index], inorder[0:index])
#         root_right_tree = self.buildTree(preorder[1+index:], inorder[index+1:])
#         root_tree.left = root_left_tree
#         root_tree.right = root_right_tree
#         return root_tree
