# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = [[root, 1]]
        minimum = float("inf")
        while stack:
            node, depth = stack.pop()
            if node:

                if not node.left and not node.right:
                    minimum = min(minimum, depth)

                if node.left:
                    stack.append([node.left, depth+1])
                if node.right:
                    stack.append([node.right, depth+1])

        print(minimum)
        return minimum
