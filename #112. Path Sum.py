# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def helper(node, sum):
            if not node:
                return False

            sum += node.val
            if not node.left and not node.right:
                return sum == targetSum

            return helper(node.left, sum) or helper(node.right, sum)

        return helper(root, 0)
