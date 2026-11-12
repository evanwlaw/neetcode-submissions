# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        good node is if pathlargest > than curr node
        """

        def dfs(node, pathLargest):
            if not node:
                return 0

            result = 1 if node.val >= pathLargest else 0
            pathLargest = max(pathLargest, node.val)

            left = dfs(node.left, pathLargest)
            right = dfs(node.right, pathLargest)
            return result + left + right
        return dfs(root, root.val)