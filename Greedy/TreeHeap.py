
class Node:
    def __init__(self, key, val, left=None, right=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self):
        return "(" + str(self.key) + "," + str(self.val) + ")"

def find_smaller(root, t):
    if not root or root.key >= t:
        return []
    res = [root]
    res += find_smaller(root.left, t)
    res += find_smaller(root.right, t)
    return res

def main():
    n1 = Node(3, 4)
    n1.left = Node(5, 1)
    n1.right = Node(6, 4)
    n1.left.left = Node(7, "idk")
    n1.right.left = Node(10, 8)
    n1.right.right = Node(7, 5)
    print(find_smaller(n1, 11))
main()