# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        result = []

        q = collections.deque([root])

        while q:
            qLen = len(q)
            s = 0
            for i in range(qLen):
                node = q.popleft()
                s += node.val
                if node:
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            result.append(s/qLen)

        return result
