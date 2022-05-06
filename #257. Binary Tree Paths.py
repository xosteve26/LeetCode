# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        l = []
        rootNode = root
        s = str(root.val)

        def helper(node, s, l):
            s += "->"+str(node.val)
            if not node.left and not node.right:
                l.append(s)
                return
            if node.left:
                helper(node.left, s, l)
            if node.right:
                helper(node.right, s, l)

        if not root.left and not root.right:
            l.append(s)
            return l
        if root.left:
            helper(root.left, s, l)
        if root.right:
            helper(root.right, s, l)
        return l
