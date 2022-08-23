#https://practice.geeksforgeeks.org/problems/top-view-of-binary-tree/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=top-view-of-binary-tree
import collections
class Solution:

    #Function to return a list of nodes visible from the top view
    #from left to right in Binary Tree.
    def topView(self, root):
        result = []
        mp = {}

        def helper(node):
            q = collections.deque([(node, 0)])

            while q:
                qLen = len(q)

                for i in range(qLen):
                    node, idx = q.popleft()

                    if node:
                        if idx not in mp:
                            mp[idx] = node.data
                        q.append((node.left, idx-1))
                        q.append((node.right, idx+1))

        helper(root)
        sMp = sorted(mp.keys())
        return [mp[key] for key in sMp]
