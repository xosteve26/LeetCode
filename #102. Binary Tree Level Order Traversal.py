# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = collections.deque([root])

        def helper(node):
            while q:
                l = []
                qLen = len(q)
                for i in range(qLen):
                    node = q.popleft()
                    if node:
                        l.append(node.val)
                        q.append(node.left)
                        q.append(node.right)
                if l:
                    res.append(l)

        helper(root)
        return res
