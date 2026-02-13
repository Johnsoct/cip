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

    def get(self, key: int) -> int:
        """Returns the value at the key or -1 if it does not exist"""

        if key < 0:
            raise ValueError("The use of negative keys are not supported")

        # If key exists in the LRU cache, make it the new Tail node and return its value

        # If it doesn't exist, return -1

        pass

    def update_node_to_MRU(self, node: ListNode):
        # Remove node from its current position
        node_next = node.next
        node_prev = node.prev

        if node.prev:
            node.prev.next = node_next

        if node.next:
            node.next.prev = node_prev

        # Add node to tail
        if self.tail:
            self.tail.next = node

        self.tail = node



    def put(self, key: int, val: int) -> None:
        """
        Add a key and its value to the cache

        If adding a key would result in exceeding the cache's capacity, evict the least recently
        used element. If the key already exists in the cache, update its value.
        """

        if val < 0:
            raise ValueError("Negative values are not supported")

        # WARN: this doesn't process ListNode access
        # Add or update the key:value in the hashmap
        self.hashmap[key] = val

        # Instantiate the head of the cache
        if not self.head:
            self.head = ListNode(val)
            return

        # Instantiate the tail of the cache
        if not self.head.next:
            self.tail = ListNode(val, prev = self.head)
            self.head.next = self.tail
            return

        # Add the new value to the cache by replacing the tail
        self.update_node_to_MRU(ListNode(val, prev = self.tail)

        # If over capacity, evict the Head node (LRU) and remove it from the hashmap
        if len(self.hashmap) > self.capacity:
            del self.hashmap[list(self.hashmap)[0]]
            
            self.head = self.head.next
            self.head.prev = None

    def values(self) -> List[int]:
        cur = self.head
        values = []

        while self.head and cur:
            print(self.head.val)
            values.append(cur.val)
            cur = self.head.next

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
