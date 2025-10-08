class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        # return the top item of the stack
        return self.stack[-1]

    def print_stack(self, message):
        print(f"{message}: {self.stack}")


# initialize the stack
stack1 = Stack()