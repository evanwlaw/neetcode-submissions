# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        """
        need to get the num of current path

                        1
                2               1
            9       2       3       4
        
        129         122     113         114


        at 2nd level node 2:
            needs to pass up 129 + 122
        at 2nd level node 1:
            needs to pass up 113 + 114
        
        so need to pass down the num of path until we hit root
        """

        def dfs(node, pathNum):
            if not node:
                return 0
            
            pathNum = pathNum * 10 + node.val

            if not node.left and not node.right:
                return pathNum
            return dfs(node.left, pathNum) + dfs(node.right, pathNum)
        
        return dfs(root, 0)