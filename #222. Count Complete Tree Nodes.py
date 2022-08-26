# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        c = [0]

        q = collections.deque([root])

        while q:
            qLen = len(q)

            for i in range(qLen):
                node = q.popleft()
                c[0] += 1
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return c[0]
