from typing import Any


class Node:
    def __init__(self, data: Any, next_=None) -> None:
        self.data = data
        self.next = next_


class Stack:
    def __init__(self) -> None:
        self.stack = None
