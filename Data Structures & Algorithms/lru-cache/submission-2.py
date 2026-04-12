class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lru_map = {}
        self.left , self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left
    
    def insert(self, node):
        prev = self.right.prev
        prev.next = node
        node.prev = prev
        node.next = self.right
        self.right.prev = node
    
    def remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def get(self, key: int) -> int:
        if self.lru_map.get(key):
            self.remove(self.lru_map[key])
            self.insert(self.lru_map[key])
            return self.lru_map[key].val
        return -1
        
    def put(self, key: int, value: int) -> None:
        if self.lru_map.get(key):
            self.remove(self.lru_map[key])

        self.lru_map[key] = Node(key,value)
        self.insert(self.lru_map[key])

        if len(self.lru_map) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.lru_map[lru.key]
            
        
