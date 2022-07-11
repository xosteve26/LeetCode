# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        tree1 = []
        tree2 = []

        def helper(node, tree):
            q = collections.deque([node])
            while q:
                qLen = len(q)

                for i in range(qLen):
                    node = q.popleft()

                    if node:
                        tree.append(node.val)
                        q.append(node.left)
                        q.append(node.right)
                    else:
                        tree.append("NONE")
            return tree

        T1 = helper(p, tree1)
        T2 = helper(q, tree2)

        return T1 == T2
