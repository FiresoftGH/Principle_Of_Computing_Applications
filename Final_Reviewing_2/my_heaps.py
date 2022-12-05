import random as rd

class Heaps:
    def __init__(self):
        self.heap = []

    def push(self, val):
        self.heap.append(val)

        index = len(self.heap) - 1

        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[parent_index] >= self.heap[index]:
                break

            else:

                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]

                index = parent_index

    def pop(self):
        
        if len(self.heap) == 0:
            return

        if len(self.heap) == 1:
            return self.heap.pop()

        self.heap[0] = self.heap.pop()

        index = 0

        while True:
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2

            if left_child_index > len(self.heap) and self.heap[left_child_index] > len(self.heap):
                index = left_child_index

            elif right_child_index > len(self.heap) and self.heap[right_child_index] > len(self.heap):
                index = right_child_index

            else:
                break

    def get(self):
        print(self.heap)
        return self.heap

def heapify(array):
    temp = Heaps()
    for element in range(len(array)):
        temp.push(array[element])

    array = temp
    return array

test = Heaps()

for x in range(10):
    rando = rd.randint(-10, 10)
    test.push(rando)

test.push(3)
test.push(4)
test.push(5)
test.get()
test.pop()
test.pop()
test.pop()
test.get()

guga = [36, 60, 84, 27, 73, 79, 0, 1, 54, 24]
new_guga = heapify(guga)
new_guga.get()
                

            

