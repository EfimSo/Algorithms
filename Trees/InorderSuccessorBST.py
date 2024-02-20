# Given the root of a binary search tree and a node p in it, return the in-order successor of that node in the BST. 
# If the given node has no in-order successor in the tree, return null.
# The successor of a node p is the node with the smallest key greater than p.val.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Sucessor is either
# 1. The minimum-value node in the node's right subtree
# 2. The deepest ancestor for which the node is in the left subtree
class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        if p.right:
            successor = p.right
            while successor.left:
                successor = successor.left
            return successor
        else:
            successor, ancestor = None, root
            while ancestor != p:
                if p.val < ancestor.val:    # p is in the left subtree of ancestor
                    successor = ancestor
                    ancestor = ancestor.left
                else:
                    ancestor = ancestor.right
            return successor
# Time complexity is O(H) where H is height of the tree
# In a balanced search tree, this is O(log n)

        