# https://www.geeksforgeeks.org/write-a-function-that-counts-the-number-of-times-a-given-int-occurs-in-a-linked-list/


class Node:
    def __init__(self, element):
        self.element = element
        self.next = None

    def set_next(self, next_element):
        self.next = next_element


class LinkedList:  # Implement a Linked List
    def __init__(self):
        self.data = None

    @staticmethod
    def _count(node, element, count=0):
        if not node.next:
            return count

        if node.element == element:
            return LinkedList._count(node.next, element, count=count + 1)
        return LinkedList._count(node.next, element, count)

    def add(self, value):
        # add at the end
        if not self.data:
            self.data = Node(value)
        else:
            last = self.get_last(self.data)
            last.set_next(Node(value))

    @staticmethod
    def get_last(node):
        # visiting the entire structure recursively - not so efficient
        # O(n) appending at the end
        # I can do O(1) if pushing at the beginning of the list instead
        if not node.next:
            return node
        return LinkedList.get_last(node.next)

    def count(self, element):
        return self._count(self.data, element)


if __name__ == "__main__":
    ll = LinkedList()
    ll.add(3)
    ll.add(4)
    ll.add(4)
    ll.add(5)

    assert ll.count(4) == 2
    assert ll.count(3) == 1
    assert ll.count(10) == 0
    print("Ok")
