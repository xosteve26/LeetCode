# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        seen = defaultdict(int)
        RESULT = []

        def dfs(node):
            if not node: return "null"

            leftSerialized = dfs(node.left)
            rightSerialized = dfs(node.right)
            serializedTree = str(node.val) + "," + leftSerialized + "," + rightSerialized

            seen[serializedTree] +=1

            if(seen[serializedTree] == 2): RESULT.append(node)

            return serializedTree

        dfs(root)
        return RESULT