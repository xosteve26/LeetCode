# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:

        def helper(node, lft):
            if not node:
                return 0

            if not node.left and not node.right:
                return node.val if lft else 0

            l = helper(node.left, True)
            r = helper(node.right, False)

            return l+r

        return helper(root, False)
