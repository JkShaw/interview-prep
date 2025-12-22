"""
LRU Cache

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:
LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.


Example 1:
Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4


Constraints:
1 <= capacity <= 3000
0 <= key <= 104
0 <= value <= 105
At most 2 * 105 calls will be made to get and put.
"""

class Node:
    def __init__(self, key, val):
        self.key = key
        self.value = val
        self.next = None
        self.previous = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lookup = {}
        self.head_node = Node(0, 0)
        self.tail_node = Node(0, 0)
        self.head_node.next = self.tail_node
        self.tail_node.previous = self.head_node

    def _remove_node(self, node_to_remove):
        previous_node = node_to_remove.previous
        next_node = node_to_remove.next
        previous_node.next = next_node
        next_node.previous = previous_node

    def _add_to_front(self, node_to_add):
        node_to_add.next = self.head_node.next
        node_to_add.previous = self.head_node
        self.head_node.next.previous = node_to_add
        self.head_node.next = node_to_add

    def get(self, key: int) -> int:
        if key in self.lookup:
            node_to_move = self.lookup[key]
            # This item was just used, so it must be moved to the front to mark it as most recent.
            self._remove_node(node_to_move)
            self._add_to_front(node_to_move)
            return node_to_move.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.lookup:
            node_to_update = self.lookup[key]
            self._remove_node(node_to_update)
            node_to_update.value = value
            self._add_to_front(node_to_update)
            return

        # If the cache is full, we must remove the least recently used item to make space.
        if len(self.lookup) == self.capacity:
            least_recent_node = self.tail_node.previous
            self._remove_node(least_recent_node)
            del self.lookup[least_recent_node.key]

        new_node = Node(key, value)
        self.lookup[key] = new_node
        self._add_to_front(new_node)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)