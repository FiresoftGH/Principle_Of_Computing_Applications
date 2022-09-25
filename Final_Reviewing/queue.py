class Queue:
    def __init__(self, size):
        self.array = []
        self.size = size

    def enqueue(self, item):
        if self.len() < self.size:
            return self.array.append(item)
        else:
            return "The Queue is full"

    def dequeue(self):
        if self.len() == 0:
            return "Queue is Empty"
        else:
            return self.array.pop(0)

    def len(self):
        return len(self.array)

    def is_empty(self):
        if self.len() == 0:
            return True
        else:
            return False

    def first(self):
        if self.len() == 0:
            return "Invalid Operation"
        else:
            return self.array[0]

    def resize(self, new_size):
        self.size = new_size
        return self.len()

    def __repr__(self):
        return str(self.array)

queue = Queue(6)

# Test case
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

# enqueue test
for element in [4, 5, 6, 7, 8, 9, 10]:
    queue.enqueue(element)

print(queue)

