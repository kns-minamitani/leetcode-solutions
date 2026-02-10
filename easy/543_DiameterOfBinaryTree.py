# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def height(node):
            nonlocal ans
            if not node:
                return 0
            left_h = height(node.left)
            right_h = height(node.right)
            
            ans = max(ans, left_h + right_h)
            
            return 1 + max(left_h, right_h)
        
        height(root)
        return ans