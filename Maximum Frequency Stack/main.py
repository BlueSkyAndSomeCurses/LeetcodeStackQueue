from typing import Any
from collections import deque


class Node:
    def __init__(self, data: Any) -> None:
        self.data = data
        self.freq = 1

    def __repr__(self):
        return f"{self.data} : {self.freq}"


class FreqStack:

    def __init__(self):
        self.freq_stack = deque()
        self.max_freq = 0
        self.max_i = 0

    def push(self, val: int) -> None:
        new_node = Node(val)
        for node in self.freq_stack:
            if node.data == val:
                new_node.freq = node.freq + 1
                break

        self.freq_stack.appendleft(new_node)

    def pop(self) -> int:
        max_i = 0
        max_freq = 0

        for i, node in enumerate(self.freq_stack):
            if node.freq > max_freq:
                max_freq = node.freq
                max_i = i

        self.freq_stack.rotate(-max_i)
        return_node = self.freq_stack.popleft()
        self.freq_stack.rotate(max_i)

        return return_node.data


freq_stack = FreqStack()
freq_stack.push(1)
freq_stack.push(0)
freq_stack.push(0)
freq_stack.push(1)
freq_stack.push(5)
freq_stack.push(4)
freq_stack.push(1)
freq_stack.push(5)
freq_stack.push(1)
freq_stack.push(6)

print(freq_stack.pop())
print(freq_stack.pop())
print(freq_stack.pop())
print(freq_stack.pop())
print(freq_stack.pop())
print(freq_stack.pop())
print(freq_stack.pop())
print(freq_stack.pop())
print(freq_stack.pop())
print(freq_stack.pop())

print("---")

freq_stack = FreqStack()
freq_stack.push(5)
freq_stack.push(7)
freq_stack.push(5)
freq_stack.push(7)
freq_stack.push(4)
freq_stack.push(5)

print(freq_stack.pop())
print(freq_stack.pop())
print(freq_stack.pop())
print(freq_stack.pop())
print(freq_stack.pop())
