class ArrayQueue:
    DEFAULT_CAPCITY = 10

    def __init__(self):
        # Create an empty queue
        self._data = [None] * ArrayQueue.DEFAULT_CAPCITY
        self._size = 0
        self._front = 0

    def __len__(self):
        # Return Queue Size
        return self._size

    def is_empty(self):
        # Return if queue is empty or not
        return self._size == 0

    def first(self):
        # Return the first element
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[self._front]

    def dequeue(self):
        # Remove and return the first element of the queue
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return answer

    def enqueue(self, e):
        # Add an element to the queue
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1
    
    def _resize(self, cap):
        # Resize to a new capacity
        old = self.data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1 + walk) % len(old)
        self._front = 0

    def __repr__(self):
        # Building the queue
        return ', '.join(str(i) for i in self._data)

if __name__ == '__main__':
    Q = ArrayQueue()
    Q.enqueue(1)
    Q.enqueue(2)
    Q.enqueue(3)
    print(Q)
