# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def graph(self,root):
        mp={}
        q=collections.deque([root])
        while q:
            curr=q.popleft()
    
            if curr not in mp:
                mp[curr]=[]
            
            if curr.left:
                #add child to parent adjList
                mp[curr].append(curr.left)
                #add parent to child adjList
                if curr.left not in mp:
                    mp[curr.left]=[]
                mp[curr.left].append(curr)
                #add child to queue
                q.append(curr.left)
            
            if curr.right:
                #add child to parent adjList
                mp[curr].append(curr.right)
                #add parent to child adjList
                if curr.right not in mp:
                    mp[curr.right]=[]
                mp[curr.right].append(curr)
                #add child to queue
                q.append(curr.right)       
        return mp
                
        
    
    
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        #edge case
        if not root or not target:
            return []
        
        if k == 0:
            return [target.val]
        
        result=[]
        adjL=self.graph(root)
        
        #BFS of the adjacency list
        q=collections.deque([target])
        d=0
        visited=set()
        while q and d<=k:
            qLen=len(q)
            for _ in range(qLen):
                node=q.popleft()
                if node not in visited:
                    for child in adjL[node]:
                        q.append(child)

                    if d == k:
                        result.append(node.val)
                visited.add(node)
                    
            d+=1

        return result
        