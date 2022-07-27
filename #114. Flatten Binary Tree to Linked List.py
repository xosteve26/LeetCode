# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def helper(node):
            if node == None:
                return None

            l = helper(node.left)
            r = helper(node.right)

            if node.left:
                node.left = None
                node.right = l

                while l.right:
                    l = l.right
                l.right = r

            return node

        helper(root)
