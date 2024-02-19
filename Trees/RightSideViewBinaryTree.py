# Given the root of a binary tree, imagine yourself standing on the right side of it.
# Return the values of the nodes you can see ordered from top to bottom.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# DFS NRL pre-order traversal
# pass level into recursive func 
# if level >= res.length, add to solution
def rightSideView(root: TreeNode) -> list[int]:
    res = []
    def recur(node, level):
        if not node:
            return
        if level >= len(res):
            res.append(node.val)
        recur(node.right, level + 1)
        recur(node.left, level + 1)
    recur(root, 0)
    return res

from collections import deque
# BFS level-order solution
def rightSideView(root: TreeNode) -> list[int]:
    if not root:
        return []
    res = []
    q = deque()
    q.append(root)
    while q:
        level_size = len(q)
        count = 0
        while count < level_size:
            node = q.popleft()
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
            count += 1
        res.append(node.val)    # add last node in level to the result
    return res