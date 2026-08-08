# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool: 
        
        def dfs(left_value, node, right_value):
            if node is None:
                return True
            if not(left_value < node.val < right_value):
                return False
            
            left_valid = dfs(left_value, node.left, node.val)
            right_valid = dfs(node.val, node.right, right_value)
            return left_valid and right_valid

        return dfs(float("-inf"), root, float("inf"))