# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        def dfs(node):
            if not node:
                return 0
            
            result = node.val if low <= node.val <= high else 0
            
            return result + dfs(node.left) + dfs(node.right)
        
        return dfs(root)