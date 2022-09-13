from collections import deque

class Stack:
    def __init__(self, data = []):
        self.data = data

    def __str__(self):
        return f'Stack is {self.data}'

    def push(self, item):
        return [item] + self.data

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[0]

    def is_empty(self):
        if len(self.data) == 0:
            return True
        else:
            return False
    
    def size(self):
        return len(self.data)

stack = Stack(["A", "B", "C"])

# Test cases

print(stack.__str__())
print(stack.pop())
print(stack.__str__())
print(stack.push("D"))
print(stack.__str__())
print(stack.is_empty())
print(stack.peek())
print(stack.size())



