from collections import deque


class FreqStack:

    def __init__(self):
        self.freq_stack = deque()
        self.stack = deque()

    def push(self, val):
        self.stack.appendleft(val)
        self.freq_stack.appendleft(self.stack.count(val))

    def pop(self):
        max_freq = 0
        max_val = 0
        for freq, val in zip(self.freq_stack, self.stack):
            if freq > max_freq:
                max_freq = freq
                max_val = val

        self.freq_stack.remove(max_freq)
        self.stack.remove(max_val)
        return max_val
