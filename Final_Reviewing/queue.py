class Queue:
    def __init__(self, array = []):
        self.array = array

    def enqueue(self, item):
        return self.array.append(item)

    def dequeue(self):
        if len(self.array) == 0:
            return "Queue is Empty"
        else:
            return self.array.pop(0)

    def len(self):
        return len(self.array)

    def is_empty(self):
        if len(self.array) == 0:
            return True
        else:
            return False

    def first(self):
        if len(self.array) == 0:
            return "Invalid Operation"
        else:
            return self.array[0]

queue = Queue([])

# Test case
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print(queue.first())
queue.dequeue()
print(queue.first())
print(queue.len())