# LRU Cache implementation

# Design requirements:
#   - fixed capacity
#   - O(1) get
#       - if not in cache, return default element
#   - O(1) put
#       - update if already in it
#       - evict least recently used if over capacity

# Components:
#   - Node(key, val), doubly-linked LL - prev, next
#   - DL LL for ordering the elements least-to-most used
#       - pointers to least and most used elements (left, right)
#   - Hash map (key: Node) - O(1) get access anywhere in LL

# Constraints:
#   - meaning of used (assume that element set to most recent on both get and put)

class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left, self.right = Node(0, 0), Node(0,0)       # dummy nodes
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
    
    def insert(self, node):
        prev, right = self.right.prev, self.right
        prev.next = right.prev = node
        node.prev, node.next = prev, right
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # make most recent element
        self.remove(self.cache[key])
        self.insert(self.cache[key]) 
        return self.cache[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]



# Usage template
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)