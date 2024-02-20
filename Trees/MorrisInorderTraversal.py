# Morris traversal O(1) space

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Morris in-order traversal
def inorderTraversal(root: TreeNode) -> list[int]:
    if not root:
        return []
    res = []
    curr = root
    while curr:
        if not curr.left:
            res.append(curr.val)
            curr = curr.right
        else:
            pred = find_predecessor(curr)
            if not pred.right:
                pred.right = curr
                # visit node here for pre-order traversal (before visiting left sub-tree)
                curr = curr.left
            else:
                pred.right = None
                res.append(curr.val)
                curr = curr.right
    return res

# Helper function that finds in-order predecessor of a node
def find_predecessor(node):
    res = node.left
    while res.right and res.right != node:
        res = res.right
    return res
