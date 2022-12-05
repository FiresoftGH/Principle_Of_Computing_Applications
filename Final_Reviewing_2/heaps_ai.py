import random as rd

# define a class for heaps
class Heap:
    def __init__(self):
        # initialize the heap with an empty list
        self.heap = []

    # method to add a new element to the heap
    def push(self, val):
        # append the new element to the end of the list
        self.heap.append(val)

        # get the index of the new element
        idx = len(self.heap) - 1

        # loop until the element is in the correct position
        # in the heap (i.e. it is greater than or equal to
        # its parent)
        while idx > 0:
            # compute the index of the parent of the current element
            parent_idx = (idx - 1) // 2

            # if the parent is greater than or equal to the current
            # element, we can stop
            if self.heap[parent_idx] >= self.heap[idx]:
                break

            # otherwise, swap the current element with its parent
            self.heap[idx], self.heap[parent_idx] = self.heap[parent_idx], self.heap[idx]

            # update the index to be that of the parent
            idx = parent_idx

    # method to remove and return the top element from the heap
    def pop(self):
        # if the heap is empty, return None
        if len(self.heap) == 0:
            return None

        # if there is only one element in the heap, return it
        if len(self.heap) == 1:
            return self.heap.pop()

        # otherwise, remove the top element from the heap
        top = self.heap[0]
        self.heap[0] = self.heap.pop()

        # get the index of the new top element
        idx = 0

        # loop until the element is in the correct position
        # in the heap (i.e. it is less than or equal to
        # its children)
        while True:
            # compute the indices of the left and right children
            left_child_idx = 2 * idx + 1
            right_child_idx = 2 * idx + 2

            # if the left child exists and is greater than the
            # current element, update the index to be that of the
            # left child
            if (left_child_idx < len(self.heap) and
                    self.heap[left_child_idx] > self.heap[idx]):
                idx = left_child_idx

            # if the right child exists and is greater than the
            # current element, update the index to be that of the
            # right child
            elif (right_child_idx < len(self.heap) and
                  self.heap[right_child_idx] > self.heap[idx]):
                idx = right_child_idx

            # otherwise, we have found the correct position for
            # the current element, so we can stop
            else:
                break

        # return the top element

    # Print out the heap
    def printheap(self):
        print(self.heap)

test = Heap()
opt = []

for x in range(10):
    rando = rd.randint(-10, 10)
    opt.append(rando)
    test.push(rando)

print(opt)
test.push(100)
test.printheap()
test.pop()
test.printheap()