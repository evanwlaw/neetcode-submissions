# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = [[root, 1]]
        res = 0

        while stack:
            node, curr_depth = stack.pop()

            if node:
                res = max(res, curr_depth)
                stack.append([node.left, curr_depth + 1])
                stack.append([node.right, curr_depth + 1])
        
        return res
        