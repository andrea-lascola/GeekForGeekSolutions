# revert a linked list

# Best solution has linear time complexity

class Node:
    """A LinkedList Node"""
    next = None

    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"Node(value={self.value}, next={self.next})"


class LinkedList:
    """A simple Linked list data structure.

    Basic Usage::
      \
      LinkedList(head=Node(value=6, next=Node(value=5, next=Node(value=4, next=Node(value=3, next=None)))))
    """
    head = None

    def __init__(self):
        pass

    def add(self, node: Node):
        if self.head:
            node.next = self.head
        self.head = node

    def __repr__(self):
        return f"LinkedList(head={self.head})"


def revert_iterative(llist: LinkedList) -> LinkedList:
    """
    Linear complexity
    Modify llist inplace - no extra space
    :param llist: input
    :return:
    """

    prev, current = None, llist.head

    while True:
        next_el = current.next if current.next else None
        current.next = None

        if prev:
            current.next = prev

        llist.head = current

        if not next_el:
            break
        prev, current = current, next_el

    return llist


if __name__ == "__main__":
    l1 = LinkedList()
    l1.add(Node(1))
    l1.add(Node(4))
    l1.add(Node(2))

    assert l1.head.value == 2

    riterative = revert_iterative(l1)

    assert riterative.head.value == 1
    assert riterative.head.next.value == 4
    assert riterative.head.next.next.value == 2

    l2 = LinkedList()
    l2.add(Node(1))
    l2.add(Node(4))
    l2.add(Node(2))
