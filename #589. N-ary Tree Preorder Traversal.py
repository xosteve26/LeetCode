"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        l = []

        def helper(node):
            if node:
                l.append(node.val)
            else:
                return

            for i in node.children:
                helper(i)

        helper(root)
        return l
