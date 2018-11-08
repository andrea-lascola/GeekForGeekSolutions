# https://www.geeksforgeeks.org/lru-cache-implementation/
import collections

Entry = collections.namedtuple('Entry', "key value")


class Node:
    def __init__(self, element, prev_element=None, next_element=None):
        self.element = element
        self.prev = prev_element
        self.next = next_element

    def set_next(self, next_element):
        self.next = next_element

    def set_prev(self, prev_element):
        self.prev = prev_element

    def __repr__(self):
        return f"<Node element={self.element}>"


class DoubleLinkedList:

    def __init__(self):
        self._size = 0
        self.head = None
        self.tail = None

    def push(self, node: Node):
        if not self.head:
            self.head = node
            self.tail = node
        else:
            node = node
            self.head.prev = node
            node.next = self.head
            self.head = node
        self._size += 1

    def remove(self, node: Node):
        prev_node, next_node = node.prev, node.next

        if prev_node and next_node:
            prev_node.next = next_node
            next_node.prev = prev_node
        elif prev_node:
            self.tail = prev_node
            prev_node.next = None
        elif next_node:
            next_node.prev = None
        self._size -= 1

    @property
    def size(self):
        return self._size


class Cache:
    def __init__(self, dimension):
        self.dimension = dimension
        self.dll = DoubleLinkedList()
        self.map = dict()

    def set(self, key: str, element):
        entry = Entry(key, element)
        print(f"Set {entry}")
        node = Node(entry)
        self.dll.push(node)
        self.map[key] = node
        self._cleanup()

    def get(self, key: str):
        node = self.map.get(key)

        if node:
            print(f"Get hit {node}")
            self.dll.remove(node)
            self.dll.push(node)
            self._cleanup()
            return node.element.value
        print(f"Get miss {key}")
        return None

    def _cleanup(self):
        while self.dll.size > self.dimension:
            print(f"Evicting {self.dll.tail}")
            del self.map[self.dll.tail.element.key]
            self.dll.remove(self.dll.tail)


if __name__ == "__main__":
    cache = Cache(dimension=3)

    cache.set("key", "key-el")
    cache.set("key1", "key-el1")
    cache.set("key2", "key-el2")

    assert cache.get("key") == "key-el"
    assert cache.get("key1") == "key-el1"

    # least recently used "key2" is removed
    cache.set("key3", "key-el3")

    assert cache.get("key2") is None

    print("Ok")
