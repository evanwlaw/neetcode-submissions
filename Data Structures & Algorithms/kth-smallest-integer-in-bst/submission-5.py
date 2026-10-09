# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        given root node of binary search tree
        find the kth node's value in tree
        
        Input: root = [2,1,3], k = 1
        Output: 1

                    2
            1               3
        return 1 as k is 1 (return first node from left)

        Input: root = [4,3,5,2,null], k = 4
        Output: 5

                    4
                3       5
            2
        return 5 as 4th node from left is 5

        need to inorder traversal

        We could keep an array of len k -> traverse entire graph and terminate when output len is k and return kth node.val -> would use O(N) space

        or keep track how many nodes to traverse when 0, return the val of our current node
                    4
                3       5
            2
        
        dfs with an variable outside the dfs function to see how many nodes we've seen/processed left
        """
        nodesLeft = k
        res = 0

        def dfs(node):
            nonlocal nodesLeft, res
            if not node:
                return


            dfs(node.left)
            nodesLeft -= 1
            if nodesLeft == 0:
                res = node.val
                return
            dfs(node.right)
            return
        dfs(root)
        return res
            

