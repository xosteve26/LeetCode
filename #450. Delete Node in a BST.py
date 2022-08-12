# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        #Find Minimum value in right sub tree
        def findMin(node):
            curr = node
            while curr.left:
                curr = curr.left
            return curr

        def helper(node, key):
            if not node:
                return None

            if key < node.val:
                node.left = helper(node.left, key)

            if key > node.val:
                node.right = helper(node.right, key)

            if node.val == key:
                if not node.left and not node.right:
                    return None

                elif not node.left:
                    return node.right

                elif not node.right:
                    return node.left

                else:
                    #Find minimum val node in right sub tree for replacement 
                    temp = findMin(node.right)
                    node.val = temp.val
                    #Delete Node that was duplicated
                    node.right = helper(node.right, temp.val)

            return node

        return helper(root, key)
