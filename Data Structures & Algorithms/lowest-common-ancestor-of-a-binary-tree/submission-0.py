# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def dfs(current_node):
            if current_node is None:
                return None
            
            if current_node.val == p.val or current_node.val == q.val:
                return current_node
            
            left_subtree = dfs(current_node.left)
            right_subtree = dfs(current_node.right)

            if left_subtree and right_subtree:
                return current_node
            
            if left_subtree and not right_subtree:
                return left_subtree
            
            if not left_subtree and right_subtree:
                return right_subtree
        
        return dfs(root)
            
            