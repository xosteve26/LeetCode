# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxi = [float("-inf")]

        def helper(node):
            if not node:
                return 0

            lh = max(0, helper(node.left))
            rh = max(0, helper(node.right))
            maxi[0] = max(maxi[0], lh+rh+node.val)

            return node.val + max(lh, rh)

        helper(root)
        return maxi[0]
