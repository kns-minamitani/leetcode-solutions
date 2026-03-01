# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque 
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []

        result = []
        dq = deque([root])

        while dq:
            level_sum = 0
            level_size = len(dq)
            for _ in range(level_size):
                node = dq.popleft()
                level_sum += node.val
                
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)

            result.append(level_sum / level_size)

        return result