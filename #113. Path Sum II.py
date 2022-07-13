# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.res = []

        def helper(node, targetSum, sum, path):
            if node:
                sum += node.val
                tmp = path+[node.val]

                if node.left:
                    helper(node.left, targetSum, sum, tmp)
                if node.right:
                    helper(node.right, targetSum, sum, tmp)

                if not node.left and not node.right and sum == targetSum:
                    self.res.append(tmp)

        helper(root, targetSum, 0, [])

        return self.res
