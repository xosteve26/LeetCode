class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = [0]

        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            res[0] = max(res[0], left + right)

            return 1 + max(left, right)

        dfs(root)
        return res[0]
