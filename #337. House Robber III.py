# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        cache = {}

        def recursion(node, stole):
            if (node, stole) in cache: return cache[(node,stole)]
            if not node: return 0

            steal, notSteal = 0, 0

            if not stole:
                steal = node.val + recursion(node.left, True) + recursion(node.right, True)
            notSteal = recursion(node.left, False) + recursion(node.right, False)

            cache[(node, stole)] = max(steal, notSteal)
            return cache[(node, stole)]

        return recursion(root, False)