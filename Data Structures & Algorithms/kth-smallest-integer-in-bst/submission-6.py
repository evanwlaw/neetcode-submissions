# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        return the kth smallest value from left

                2
            1       3
        k = 1 -> return 1

                4
            3       5
        2
        k = 4 -> return 5

        so need to do inorder traversal (dfs)
        """
        seenNodes = k
        res = 0
        def findKth(node):
            nonlocal seenNodes, res

            if not node:
                return

            findKth(node.left)
            seenNodes -= 1
            if seenNodes == 0:
                res = node.val
                return 
            
            findKth(node.right)
            return
        findKth(root)
        return res

