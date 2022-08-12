# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr = root

        while curr:
            # look into right subtree
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            # look into left subtree
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            # if p,q are in different subtrees, this is the LCA
            else:
                return curr
