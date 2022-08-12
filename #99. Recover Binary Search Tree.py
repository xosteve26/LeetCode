# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        t = []

        def helper(node):
            if not node:
                return True

            helper(node.left)
            t.append(node)
            helper(node.right)

        helper(root)
        srt = [i.val for i in t]
        srt.sort()

        for i in range(len(srt)):
            t[i].val = srt[i]
