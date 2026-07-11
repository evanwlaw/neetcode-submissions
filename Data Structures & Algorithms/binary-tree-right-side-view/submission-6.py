from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        '''
        BFS each level.

        if len(queue) - 1:
            append to res

        '''
        output = []	
        if root is None:
            return output

        queue = deque([root])
        
        while queue:
            level_len = len(queue)
            for i in range(level_len):
                node = queue.popleft()

                if i == level_len - 1:
                    output.append(node.val)
                    
                # add child nodes if existing
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return output
		

