# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        dfs

        scan for the node in root that is the same as subroot.

        then dfs to compare subtrees


        """

        def subTreedfs(p, q):
            if not p and not q:
                return True
            if not p or not q or p.val != q.val:
                return False
            
            return (subTreedfs(p.left, q.left) and 
                    subTreedfs(p.right, q.right))

        def findRootStart(node):            
            if not node:
                return False

            if subTreedfs(node, subRoot):
                return True
            
            return findRootStart(node.left) or findRootStart(node.right)
        
    
        return findRootStart(root)

