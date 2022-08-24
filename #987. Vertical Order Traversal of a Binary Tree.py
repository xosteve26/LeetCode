# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:

        result = []
        mp = defaultdict(list)

        def helper(node):
            q = collections.deque([(node, 0, 0)])

            while q:
                qLen = len(q)

                for i in range(qLen):
                    node, v, r = q.popleft()

                    if node:
                        mp[(v, r)].append(node.val)
                        q.append((node.left, v-1, r+1))
                        q.append((node.right, v+1, r+1))

        helper(root)
        cols = defaultdict(list)
        sMp = sorted(mp, key=lambda x: x[0])
        for rc in sMp:
            if rc[0] not in cols:
                for k, v in mp.items():
                    if rc[0] == k[0]:
                        cols[k[0]].extend(sorted(v))

        return list(cols.values())
