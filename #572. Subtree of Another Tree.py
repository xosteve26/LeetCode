# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root, subRoot) -> bool:
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False

        return self.isSameTree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right,subRoot)

    def isSameTree(self, tree1, tree2):
            if not tree1 and not tree2:
                return True
            if not tree1 or not tree2:
                return False
            
            return tree1.val == tree2.val and self.isSameTree(tree1.left, tree2.left) and self.isSameTree(tree1.right, tree2.right)