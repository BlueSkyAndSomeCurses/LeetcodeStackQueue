class Node:
    def __init__(self, item, next_=None):
        self.item = item
        self.next = next_


class Stack:

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def push(self, item):
        self.head = Node(item, self.head)

    def pop(self):
        item = self.head.item
        self.head = self.head.next
        return item

    @property
    def peek(self):
        return self.head.item

    def __len__(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

    def __str__(self):
        s = ""
        cur = self.head
        while cur is not None:
            s = str(cur.item) + " " + s
            cur = cur.next
        return "bottom -> " + s + "<- top"


class MyQueue:

    def __init__(self):
        self.queue = Stack()

    def push(self, x: int) -> None:

        tmp_stack = Stack()
        while not self.queue.is_empty():
            tmp_stack.push(self.queue.pop())

        tmp_stack.push(x)
        while not tmp_stack.is_empty():
            self.queue.push(tmp_stack.pop())

    def pop(self) -> int:
        return self.queue.pop()

    def peek(self) -> int:
        return self.queue.peek

    def empty(self) -> bool:
        return self.queue.is_empty()


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
obj.push(2)
obj.push(3)
print(obj.pop())
print(obj.pop())

print(obj.empty())
print(obj.peek())
obj1 = obj.pop()
