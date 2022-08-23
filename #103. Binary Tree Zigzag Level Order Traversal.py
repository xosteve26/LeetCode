# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result=[]
        
        def helper(node):
            q=collections.deque([node])
            normal=True
            while q:
                qLen=len(q)
                
                l=[float("inf")]*qLen
                for i in range(qLen):
                    node=q.popleft()
                    if node:
                        if node.left:
                            q.append(node.left)
                        if node.right:
                            q.append(node.right)
                        
                        if normal:
                            l[i]=node.val
                        else:
                            l[(qLen-1)-i]=node.val
                            
                normal=not normal    
                if l and l[0]!=float("inf"):
                    result.append(l)
                    
                
        helper(root)        
        return result