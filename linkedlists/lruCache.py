class DoublyLinkedListNode:
    def __init__(self, key: int, val: int):
        self.key = key
        self.next = None
        self.prev = None
        self.val = val

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

        # Instantiate with dummy nodes to simplify put and get operations
        self.head = DoublyLinkedListNode(-1, -1)
        self.tail = DoublyLinkedListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_node_to_MRU(self, node):
        """
        Adds the node to the tail of the cache

        Since our head and tail nodes are permanent dummy nodes, we're effectively treating
        the nodes after the head and before the tail node as the head and tail node, so here
        we need to add the node immediately before self.tail.
        """

        old_tail = self.tail.prev

        node.next = self.tail
        node.prev = old_tail
        old_tail.next = node
        self.tail.prev = node

    def get(self, key: int) -> int:
        """Returns the value at the key or -1 if it does not exist"""

        if key < 0:
            raise ValueError("The use of negative keys are not supported")

        if key not in self.hashmap:
            return -1;

        # If key exists in the LRU cache, make it the new Tail node and return its value
        node = self.hashmap[key]

        self.move_node_to_MRU(node)

        return node.val

    def move_node_to_MRU(self, node: DoublyLinkedListNode):
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
            self.remove_node(self.hashmap[key])

        node = DoublyLinkedListNode(key, val)

        # Add new value to hashmap
        self.hashmap[key] = node

        if self.capacity < len(self.hashmap):

            # Remove the LRU
            self.remove_LRU()

        # Add new node to tail
        self.add_node_to_MRU(node)

    def remove_node(self, node: DoublyLinkedListNode):
        """Removes the node from the cache's linked list"""

        if node.prev:
            node.prev.next = node.next

        if node.next:
            node.next.prev = node.prev

    def remove_LRU(self):
        """Removes the LRU node from the cache's linked list and deletes its key from the hashmap"""

        del self.hashmap[self.head.next.key]
        self.remove_node(self.head.next)

def test_lru_cache_one():
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
    output = []

    for operation in operations:
        result = operation()

        if result != None:
            output.append(result)

    assert output == [250, 300, -1]

def test_lru_cache_two():
    cache = LRUCache(2)
    operations = [
            lambda: cache.put(1, 1),
            lambda: cache.put(2, 2),
            lambda: cache.get(1),
            lambda: cache.put(3, 3),
            lambda: cache.get(2),
            lambda: cache.put(4, 4),
            lambda: cache.get(1),
            lambda: cache.get(3),
            lambda: cache.get(4),
    ]
    output = []

    for operation in operations:
        result = operation()

        if result != None:
            output.append(result)

    assert output == [1, -1, -1, 3, 4]
