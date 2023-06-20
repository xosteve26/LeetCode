# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def recursion(node):
            if not node:
                return 0

            leftHeight = recursion(node.left)
            rightHeight = recursion(node.right)

            if(leftHeight == -1 or rightHeight == -1):
                return -1
            if(abs(leftHeight-rightHeight) > 1):
                return -1

            return 1 + max(leftHeight, rightHeight)

        return True if recursion(root) != -1 else False
