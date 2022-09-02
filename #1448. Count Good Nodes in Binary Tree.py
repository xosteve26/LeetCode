# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        result=[0]
        
        def helper(node,mx):
            if not node:
                return
            
            if node.val>=mx:
                result[0]+=1
            mx=max(mx,node.val)
            
            helper(node.left,mx)  
            helper(node.right,mx)
                
        helper(root,root.val)
        return result[0]
        