# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invert_recur(self, tree: Optional[TreeNode]) -> Optional[TreeNode]:
        if tree is None:
            return

        tmp = tree.left
        tree.left = tree.right
        tree.right = tmp

        if tree.left is not None:
            self.invert_recur(tree.left)

        if tree.right is not None:
            self.invert_recur(tree.right)

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.invert_recur(root)
        return root

        
