class Node:
    def __init__(self, item, next=None):
        self.item = item
        self.next = next


class Queue:

    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def add(self, item):
        if self.head is None:
            self.tail = Node(item)
            self.head = self.tail
        else:
            self.tail.next = Node(item)
            self.tail = self.tail.next

    def pop(self):
        if self.head:
            item = self.head
            self.head = self.head.next
            return item.item
        raise ValueError("Queue is empty.")

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
        current = self.head
        while current is not None:
            s += str(current.item) + " "
            current = current.next
        return f"start -> {s}<- end"


class MyStack:

    def __init__(self):
        self.stack = Queue()

    def push(self, x: int) -> None:
        tmp_queue = Queue()
        tmp_queue.add(x)

        while not self.stack.is_empty():
            tmp_queue.add(self.stack.pop())

        self.stack = tmp_queue

    def pop(self) -> int:
        return self.stack.pop()

    def top(self) -> int:
        if not self.stack.is_empty():
            return self.stack.peek

    def empty(self) -> bool:
        return self.stack.is_empty()


# Your MyStack object will be instantiated and called as such:
obj = MyStack()

obj.push(1)
obj.push(2)
obj.push(3)

print(obj.pop())
print(obj.pop())
print(obj.top())
print(obj.empty())
print(obj.pop())
print(obj.empty())
print(obj.top())
