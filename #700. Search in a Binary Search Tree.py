# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        def helper(node):
            if not node:
                return None

            if node.val == val:
                return node

            if val < node.val:
                node = helper(node.left)
            elif val > node.val:
                node = helper(node.right)

            return node

        return helper(root)
