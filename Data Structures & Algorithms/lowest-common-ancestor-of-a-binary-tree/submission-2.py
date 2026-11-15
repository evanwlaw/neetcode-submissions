# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
                        5
                3               4
        2               1

        p = 1, q = 2 -> reutrn 3

        if p in left and q in right -> return curr node

        if p and q in left -> move node to left
        if p and q in right -> move ndoe to right
        """

        def dfs(node):
            if not node:
                return None
            
            if node.val == p.val or node.val == q.val:
                return node
            
            left = dfs(node.left)
            right = dfs(node.right)

            if left and right:
                return node
            
            if left and not right:
                return left
            
            if right and not left:
                return right
            
        return dfs(root)