# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        queue = deque([[root, 0, 0]])
        MAXIMUM_WIDTH = float("-inf")
        prevLevel, firstNum = 0, 0
        while queue:
            for _ in range(len(queue)):
                node, idx, level = queue.popleft()

                if level > prevLevel:
                    prevLevel = level
                    firstNum = idx

                MAXIMUM_WIDTH = max(MAXIMUM_WIDTH, idx - firstNum + 1)

                if node.left:
                    queue.append([node.left, 2 * idx, level + 1])
                if node.right:
                    queue.append([node.right, 2 * idx + 1, level + 1])

        return MAXIMUM_WIDTH
