import queue


class Queue:
    def __init__(self):
        # Using 2 LIFO Stacks
        self.stack_in = queue.LifoQueue()
        self.stack_out = queue.LifoQueue()

    def push(self, element):
        self.stack_in.put(element)

    def pop(self):
        if self.stack_out.empty():
            # Move stack_in into stack_out
            while not self.stack_in.empty():
                self.stack_out.put(self.stack_in.get())

        return self.stack_out.get()


if __name__ == "__main__":
    q = Queue()

    q.push(3)
    q.push(2)
    q.push(1)

    assert q.pop() == 3
    assert q.pop() == 2

    q.push(5)

    assert q.pop() == 1
    assert q.pop() == 5

    print("Ok")
