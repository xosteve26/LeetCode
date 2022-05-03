# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def check(leftSubTree, rightSubTree):

            if (leftSubTree == None and rightSubTree == None):
                return True
            elif(leftSubTree != None and rightSubTree != None):
                return leftSubTree.val == rightSubTree.val and check(leftSubTree.left, rightSubTree.right) and check(leftSubTree.right, rightSubTree.left)
            return False

        x = check(root.left, root.right)
        return x
