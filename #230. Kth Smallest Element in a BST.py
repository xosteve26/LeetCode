# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        heap = []

        def helper(node):

            if not node:
                return None
            helper(node.left)
            heap.append(node.val)
            helper(node.right)

        helper(root)
        while heap and k-1 > 0:
            heap.pop(0)
            k -= 1

        return heap[0]
