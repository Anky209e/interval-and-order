class _Node:
    """Init for Doubley Linked list with both prev and next"""
    def __init__(self,key=None,value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self,capacity):
        if not isinstance(capacity,int) or capacity < 0:
            raise ValueError("capacity must be integer and non-negative number")
        self.capacity = capacity
        self._nodes = {}
        
        # Least Recently used head
        self._head = _Node()
        # Most recently used tail
        self._tail = _Node()
        
        self._head.next = self._tail
        self._tail.prev = self._head

    def _append(self,node):
        previous = self._tail.prev
        previous.next = node
        node.prev = previous
        node.next = self._tail
        self._tail.prev = node

    def _remove(self,node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self,key):
        
        # Gets value from dict
        node = self._nodes.get(key)
        # If does not exists return -1
        if node is None:
            return -1
        
        self._remove(node)
        self._append(node)
        return node.value

    
    def put(self,key,value):
        node = self._nodes.get(key)
        if node is not None:
            node.value = value
            self._remove(node)
            self._append(node)
            return
        if self.capacity == 0:
            return
        if len(self._nodes) == self.capacity:
            oldest = self._head.next
            self._remove(oldest)
            del self._nodes[oldest.key]
        node = _Node(key,value)
        self._nodes[key] = node
        self._append(node)
        

if __name__ == "__main__":
    lru_cache = LRUCache(2)
    lru_cache.put(1,100)
    lru_cache.put(2,200)

    print("get(1):",lru_cache.get(1)) # 100: becomes most recently used

    lru_cache.put(3,300) # This removes 2 since it is least recently used
    print("get(2) after removal:",lru_cache.get(2)) # -1
    lru_cache.put(1,100) # promote key 1
    print("get(1) after update:",lru_cache.get(1)) # 100
    print("get(3):",lru_cache.get(3))



    




