# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def findBottomLeftValue(self, root) -> int:
        if not root:
            return None

        if not root.left and not root.right:
            return root.val

        queue = deque()
        queue.append(root)

        while queue:
            leftMost = None
            for i in range(len(queue)):
                node = queue.popleft()

                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)

                leftMost = node

        return leftMost.val
