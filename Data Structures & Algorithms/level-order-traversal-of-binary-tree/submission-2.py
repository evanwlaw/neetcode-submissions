# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        queue = deque([root])
        output = []
        while queue:
            temp = []

            #bfs through one layer at a time
            for _ in range(len(queue)):
                curr_node = queue.popleft()
                temp.append(curr_node.val)
                # push child nodes to queue if any
                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)
            output.append(temp)
        return output

            

        