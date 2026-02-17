# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def subtree_sum(node):
            if not node:
                return 0
            
            left = subtree_sum(node.left)
            right = subtree_sum(node.right)

            self.ans += abs(left - right)

            return left + right + node.val
        
        subtree_sum(root)
        return self.ans