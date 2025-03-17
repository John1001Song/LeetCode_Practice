class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = dict()
        self.cap = capacity
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        # initialize the double link
        self.head.next = self.tail
        self.tail.prev = self.head

    # support func to update doubly linked list 
    def _add_to_front(self, node):
        # when an operation applied on a element, add this element to head of the double link
        node.prev = self.head # attach this new node to head 
        node.next = self.head.next # attach old node as new node next
        self.head.next.prev = node # update old node prev as new node 
        self.head.next = node # assign new node as the new next for head
        
    def _remove(self, node):
        # when an opearion applied on an element, need to remove it from link first (in the put func to call add to front and put it back)
        # additional scenario, when an element called, the least used should be removed and this least used element is not called 
        node.prev.next = node.next
        node.next.prev = node.prev
        # should delete this node 
        
    def get(self, key: int) -> int:
        if key in self.cache:
            cur_node = self.cache[key]
            self._remove(cur_node)
            self._add_to_front(cur_node)
            return cur_node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # consider the simpliest scenario: node in dict
        if key in self.cache:
            # get this node
            cur_node = self.cache[key]
            cur_node.value = value
            self._remove(cur_node)
            self._add_to_front(cur_node)
            self.cache[key] = cur_node
            return
        else:
            # node not in the cache
            # if over size limit, remove least used node
            if len(self.cache) >= self.cap:
                least_used = self.tail.prev
                self._remove(least_used)
                del self.cache[least_used.key]
            # now, space allowed
            new_node = Node(key, value)
            self._add_to_front(new_node)
            self.cache[key] = new_node

        # # remove least used one when cache full
        # if len(self.cache.keys()) >= self.cap:
        #     least_used_node = self.tail.prev
        #     self._remove(least_used_node)
        #     del self.cache[least_used_node.key]
        # # enough space to add new node now
        # # if new node not in the cache
        # if key not in self.cache:
        #     new_node = Node(key, value)
        #     self.cache[key] = new_node
        #     self._add_to_front(new_node)
        # # if new node in the cache
        # else:
        #     # bug: if the node exists in dict but due to cache size reason, it got deleted
        #     self._remove(Node(key, value))
        #     self._add_to_front(Node(key, value))