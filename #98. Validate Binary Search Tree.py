# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def helper(lower, upper, node):
            if node == None:
                return True

            if node.val <= lower or node.val >= upper:
                return False

            return helper(lower, node.val, node.left) and helper(node.val, upper, node.right)

        return helper(float("-inf"), float("inf"), root)
