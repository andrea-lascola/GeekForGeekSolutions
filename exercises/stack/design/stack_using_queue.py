# https://www.geeksforgeeks.org/implement-a-stack-using-single-queue/
import queue


class Stack:
    def __init__(self):
        self.queue = queue.Queue()

    def push(self, element):
        self.queue.put(element)

    def pop(self):
        # get queue size
        qsize = self.queue.qsize()

        # rotate elements in the queue, getting last one inserted
        # and reinserting all popped elements
        for x in range(qsize):
            element = self.queue.get()
            if x == qsize - 1:
                return element
            self.queue.put(element)


if __name__ == "__main__":
    stack = Stack()

    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.pop() == 3

    stack.push(10)

    assert stack.pop() == 10
    assert stack.pop() == 2
    assert stack.pop() == 1

    print("Ok")
