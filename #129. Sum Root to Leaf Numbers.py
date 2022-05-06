# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def helper(node,n):
            if not node:
                return 0
            
            n=n*10+node.val
            if not node.left and not node.right:
                return n
            return helper(node.left,n) + helper(node.right,n)
        return helper(root,0)
            
            
            
            
        