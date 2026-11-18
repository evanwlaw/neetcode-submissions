# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(leftVal, node, rightVal):
            if not node:
                return True
            
            if not leftVal < node.val < rightVal:
                return False
            left = dfs(leftVal, node.left, node.val)
            right = dfs(node.val, node.right, rightVal)
            return left and right

        return dfs(float("-inf"), root, float("inf"))           