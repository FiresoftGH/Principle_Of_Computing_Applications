class LinkedStack:

    # Node Class
    class Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):

        # Create an empty stack
        self._head = None
        self._size = 0
    
    def __len__(self):

        # Return the number of elements in the stack
        return self._size

    def is_empty(self):

        # Return if the stack is empty or not
        return self._size == 0

    def push(self, e):

        # Add element e to the top of the stack
        self._head = self.Node(e, self._head)
        self._size += 1
    
    def top(self):
        
        # Return the top element of the stack
        if self.is_empty():
            raise Empty("Stack is empty")

        return self._head._element

    def pop(self):

        # Remove and return the element from the top of the stack
        if self.is_empty():
            raise Empty("Stack is empty")

        answer = self._head._element
        self._head - self._head._next
        self._size -= 1
        return answer

class LinkedQueue:

    class Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next
    
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def is_empty(self):

        return self._size == 0

    def first(self):
        
        if self.is_empty():
            raise Empty('Queue is empty')

        return self._head._element

    def dequeue(self):

        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._head._element
        self._head = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return answer

    def enqueue(self, e):

        newest = self.Node(e, None)
        if self.is_empty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1

class CircularQueue:

    class Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._tail = None
        self._size = 0
    
    def __len__(self):

        return self._size

    def is_empty(self):
        
        return self._size == 0

    def first(self):

        if self.is_empty():
            raise Empty('Queue is empty')
        head = self._tail._next
        return head._element
        
    def dequeue(self):

        if self.is_empty():
            raise Empty('Queue is empty')
        oldhead = self._tail._next
        if self._size == 1:
            self._tail = None
        else:
            self._tail._next = oldhead._next
        self._size -= 1
        return oldhead._element

    def enqueue(self, e):

        newest = self.Node(e, None)
        if self.is_empty():
            newest._next = newest
        else:
            newest._next = self._tail._next
            self._tail._next = newest
        self._tail = newest
        self._size += 1
    
    def rotate(self):
        if self._size > 0:
            self._tail = self._tail._next

stack = LinkedStack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.top())
print(stack)

queue = LinkedQueue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue())
print(queue)
