class Stack:

    def __init__(self) -> None:
        self.enclosed = []

    def push(self, value):
        self.enclosed.append(value)

    def pop(self):
        return self.enclosed.pop(-1) if self.enclosed else None

    def peek(self):
        return self.enclosed[-1] if self.enclosed else None

    def size(self):
        return len(self.enclosed)


class MyQueue(object):
    """
    Challenge:
    https://www.hackerrank.com/challenges/ctci-queue-using-two-stacks/problem
    """
    def __init__(self):
        self.stack_public = Stack()
        self.stack_buffer = Stack()

    def peek(self):
        self._update_public()
        return self.stack_public.peek()

    def pop(self):
        self._update_public()
        return self.stack_public.pop()

    def _update_public(self):
        if self.stack_public.size() == 0:
            self._transfer(self.stack_buffer, self.stack_public)

    def put(self, value):
        self.stack_buffer.push(value)

    @staticmethod
    def _transfer(source, destination):
        next_val = source.pop()
        while next_val is not None:
            destination.push(next_val)
            next_val = source.pop()


queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())