def Paths(root):
    # don't print new line

    #code here
    result = []

    def helper(node, l):

        if not node:
            return None
        l.append(node.data)

        if not node.left and not node.right:
            result.append(l[:])

        helper(node.left, l)
        helper(node.right, l)
        l.pop()

    helper(root, [])
    return result
