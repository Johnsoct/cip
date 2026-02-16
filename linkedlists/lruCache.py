from listNode import ListNode
from typing import List

class LRUCache:
    def __init__(self, capacity: int):
        """
        Creates a static sized LRU cache and a corresponding hashmap for O(1) access.

        Assumes the Head node is the LRU and Tail node is the MRU.

        Must support the following operations:
        1. Evicting a node from the cache
        2. Adding a node to the cache at the tail
        3. Moving a node from any place in the cache to the tail
        4. Accessing a node with a key
        """
        if capacity < 0:
            raise ValueError("Cannot create a LRUCache of negative size")

        self.capacity = capacity
        self.hashmap = {}
        self.head: ListNode | None = None
        self.tail: ListNode | None = None

    def add_node_to_MRU(self, node):
        """Adds the node to the tail of the cache"""

        if self.tail:
            self.tail.next = node

        self.tail = node


    def get(self, key: int) -> int:
        """Returns the value at the key or -1 if it does not exist"""

        if key < 0:
            raise ValueError("The use of negative keys are not supported")

        # If key exists in the LRU cache, make it the new Tail node and return its value
        if key in self.hashmap:

            node = self.hashmap[key]
            self.move_node_to_MRU(node)

            return node.val

        # If it doesn't exist, return -1
        else:
            return -1

    def move_node_to_MRU(self, node: ListNode):
        """Moves the node from it's current position to the tail"""

        self.remove_node(node)
        self.add_node_to_MRU(node)

    def put(self, key: int, val: int) -> None:
        """
        Add a key and its value to the cache

        If adding a key would result in exceeding the cache's capacity, evict the least recently
        used element. If the key already exists in the cache, update its value.
        """

        if val < 0:
            raise ValueError("Negative values are not supported")



        if key in self.hashmap:

            # Update the key:value in the hashmap
            self.hashmap[key].val = val

            # Update the node's position to the tail
            self.move_node_to_MRU(self.hashmap[key])

        else:

            # Instantiate the head of the cache
            if not self.head:
                node = ListNode(val)

                self.head = node
                self.hashmap[key] = node

                return

            node = ListNode(val, prev = self.tail)

            # Instantiate the tail of the cache
            if not self.head.next:
                self.tail = node
                self.head.next = self.tail
                self.hashmap[key] = node

                return

            if self.capacity == len(self.hashmap):

                # Remove the LRU
                self.remove_LRU()

                # Add new value to hashmap
                self.hashmap[key] = node

                # Add new node to tail
                self.add_node_to_MRU(node)
            
            else:

                # Add new value to hashmap
                self.hashmap[key] = node

                # Add new node to tail
                self.add_node_to_MRU(node)

    def remove_node(self, node: ListNode):
        """Removes the node from the cache's linked list"""

        node_next = node.next
        node_prev = node.prev

        if node.prev:
            node.prev.next = node_next

        if node.next:
            node.next.prev = node_prev

    def remove_LRU(self):
        """Removes the LRU node from the cache's linked list and deletes its key from the hashmap"""

        key = list(self.hashmap)[0]
        node = self.hashmap[key]

        del self.hashmap[key]
        self.remove_node(node)

    def values(self) -> List[int]:
        """Returns a list of the hashmaps values' values"""

        cur = self.head
        values = []

        while self.head and cur:
            values.append(cur.val)
            cur = cur.next

        return values

def test_lru_cache():
    cache = LRUCache(3)
    operations = [
            lambda: cache.put(1, 100),
            lambda: cache.put(2, 250),
            lambda: cache.get(2),
            lambda: cache.put(4, 300),
            lambda: cache.put(3, 200),
            lambda: cache.get(4),
            lambda: cache.get(1),
    ]

    for operation in operations:
        operation()

    assert cache.values() == [250, 300, -1]
