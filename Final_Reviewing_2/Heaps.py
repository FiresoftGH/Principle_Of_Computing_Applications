# Reference: https://www.section.io/engineering-education/heap-data-structure-python/
import random as rd
class MaxHeap:
    # Initialize the heap
    def __init__(self):
        self.heap = []

    # The parent is located at floor((i - 1/2)
    def getParentPosition(self, i):
        return int((i - 1/2))

    # The left child is located at 2i + 1
    def getleftChildPosition(self, i):
        return 2 * i + 1

    # The right child is located at 2i + 2
    def getRightChildPosition(self, i):
        return 2 * i + 2

    # Check if a given node has a parent or not
    def hasParent(self, i):
        return self.getParentPosition(i) < len(self.heap)

    # Check if a given node has a left child or not
    def hasLeftChild(self, i):
        return self.getLeftChildPositon(i) < len(self.heap)

    # Check if a given node has a right child or not
    def hasRightChild(self, i):
        return self.getRightChildPosition(i) < len(self.heap)

    # insert an item to the list
    def insert(self, key):
        self.heap.append(key) # Add the item using append
        self.heapify(len(self.heap) - 1) # Maintain the heap data structure

    # Get the maximum value of the heap
    def getMax(self):
        return self.heap[0]

    def heapify(self, i):
        # Loop until it reaches a leaf node
        while self.hasParent(i) and self.heap[i] > self.heap[self.getParentPosition(i)]:
            # Swap the values to maintain the heap data structure
            self.heap[i], self.heap[self.getParentPosition(i)] = self.heap[self.getParentPosition(i)], self.heap[i]
            # Reset the position
            i = self.getParentPosition(i)

    # Print out the heap data structure
    def printHeap(self):
        print(self.heap)

heap = MaxHeap()
for x in range(8):
    operator = rd.randint(-100, 100)
    print(operator)
    heap.insert(operator)

heap.printHeap()