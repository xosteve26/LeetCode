# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        heap = []

        def helper(node):

            if not node:
                return None

            helper(node.left)
            heap.append(node.val)
            helper(node.right)

        helper(root)
        heap.sort()
        s = -1
        c = 0
        print(heap)
        for i in heap:
            if i != s:
                s = i
                c += 1
                print(s)
            if c == 2:
                return s
        return -1
