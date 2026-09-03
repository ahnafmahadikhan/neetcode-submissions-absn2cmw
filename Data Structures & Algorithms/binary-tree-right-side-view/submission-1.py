# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from unittest import result


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        from collections import deque
        
        if not root:
            return []
        
        result = []
       
        queue = deque([root])

        while queue:

            total_len = len(queue)
            
            for x in range(total_len):

                node = queue.popleft()

                if x == total_len - 1:
                    result.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

        return result

        