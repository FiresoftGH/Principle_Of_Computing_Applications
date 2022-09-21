from types import NoneType


class Stack:
    def __init__(self, data = []):
        self.data = data

    def __str__(self):
        return f'{self.data}'

    def push(self, item):
        return self.data.insert(0, item)

    def pop(self, index):
        if len(self.data) == 0:
            return "Stack is Empty"
        else:
            return self.data.pop(index)

    def peek(self):
        if len(self.data) == 0:
            return "Stack is Empty"
        else:
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

# Emptying the stack

print(stack.pop())
print(stack.pop())
print(stack.size())
print(stack)

# See error
print(stack.pop(0)) 


