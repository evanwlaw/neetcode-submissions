# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = [[root, 1]]
        ans = 0

        while stack:
            node, height = stack.pop()
            if node:
                ans = max(ans, height)
                stack.append([node.left, height+1])
                stack.append([node.right, height+1])
        return ans
            