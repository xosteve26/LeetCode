# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = []

        q = collections.deque([root])

        while q:
            qLen = len(q)
            result.append(float("-inf"))
            for i in range(qLen):
                node = q.popleft()
                result[-1] = max(result[-1], node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return result
