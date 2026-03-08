# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        self.ans = float('inf')
        min_val = root.val

        def DFS(node):
            if not node:
                return
            
            if min_val < node.val < self.ans:
                self.ans = node.val
            DFS(node.left)
            DFS(node.right)

        DFS(root)
        return self.ans if self.ans < float('inf') else -1