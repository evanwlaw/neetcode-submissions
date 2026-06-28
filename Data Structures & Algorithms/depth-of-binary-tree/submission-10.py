# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        '''
        max_depth = 1

        base case -> None. Return max_depth

        dfs left (node, max_depth)
        dfs right (node, max_depth)

        max_depth = max(left, right)

        '''
        

        def dfs(node: TreeNode, max_depth: int):
            # base case
            if node is None:
                return max_depth
            

            left = dfs(node.left, max_depth + 1)            
            right = dfs(node.right, max_depth + 1)

            return max(left, right)
        return dfs(root, 0)