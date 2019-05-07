#Time Limit Exceeded
def move(m, arr, key, value):
    for i in range(m[key]['index']+1, len(arr)):
        arr[i - 1] = arr[i]
        m[arr[i-1]]['index'] = i - 1
    arr[len(arr) - 1] = key
    if value != None:
        m[key]['val'] = value
    m[key]['index'] = len(arr) -1

class LRUCache:

    def __init__(self, capacity: int):
        self.m = {}
        self.capacity = capacity
        self.rank = []

    def get(self, key: int) -> int:
        if key not in self.m:
            return -1
        move(self.m, self.rank, key, None)
        return self.m[key]['val']

    def put(self, key: int, value: int) -> None:
        if key in self.m:
            move(self.m, self.rank, key, value)
        else:        
            if len(self.m.keys()) < self.capacity:
                    self.m[key] = {
                        'index': len(self.rank),
                        'val': value
                    }
                    self.rank.append(key)
            else:
                self.m.pop(self.rank[0], None)
                self.rank = self.rank[1:len(self.rank)] + [key]
                for i,r in enumerate(self.rank[0:(len(self.rank)-1)]):
                    self.m[r]['index'] = i 
                self.m[key] = {
                    'index': len(self.rank) - 1,
                    'val': value
                }


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)



#链表+map
class Node:
    def __init__(self, k, v):
        self.v = v
        self.k = k
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.m = {}
        self.capacity = capacity
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.m:
            return -1
        self._remove(self.m[key])
        self._add(self.m[key])
        return self.m[key].v

    def put(self, key: int, value: int) -> None:
        if key in self.m:
            self.m[key].v = value
            self._remove(self.m[key])
            self._add(self.m[key])
        else:        
            if len(self.m.keys()) == self.capacity:
                n = self.head.next
                self._remove(n)
                del self.m[n.k]
            n = Node(key, value)
            self._add(n)
            self.m[key] = n
    
    def _add(self, node):
        p = self.tail.prev
        p.next = node
        node.next = self.tail
        node.prev = p
        self.tail.prev = node
    
    def _remove(self, node):
        n = node.next
        p = node.prev
        p.next = n
        n.prev = p

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


class Node:
    def __init__(self, k, v):
        self.v = v
        self.k = k
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.m = {}
        self.capacity = capacity
        self.head = {}
        self.tail = {}
        self.head['next'] = self.tail
        self.tail['prev'] = self.head

    def get(self, key: int) -> int:
        if key not in self.m:
            return -1
        self._remove(self.m[key])
        self._add(self.m[key])
        return self.m[key]['v']

    def put(self, key: int, value: int) -> None:
        if key in self.m:
            self.m[key]['v'] = value
            self._remove(self.m[key])
            self._add(self.m[key])
        else:        
            if len(self.m.keys()) == self.capacity:
                n = self.head['next']
                self._remove(n)
                del self.m[n['k']]
            n = { 'k': key, 'v': value}
            self._add(n)
            self.m[key] = n
    
    def _add(self, node):
        p = self.tail['prev']
        p['next'] = node
        node['next'] = self.tail
        node['prev'] = p
        self.tail['prev'] = node
    
    def _remove(self, node):
        n = node['next']
        p = node['prev']
        p['next'] = n
        n['prev'] = p

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
