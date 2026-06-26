# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None

        if root == p or root == q:
            return root
        
        left_subtree = self.lowestCommonAncestor(root.left, p, q)
        right_subtree = self.lowestCommonAncestor(root.right, p, q)

        if left_subtree and right_subtree:
            return root
        return left_subtree if left_subtree else right_subtree
