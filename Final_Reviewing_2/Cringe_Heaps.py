testarray = [-6, 4, -10, 2, -5, 7, 4, -5, 9, -1]

def addelement(e, heap):
    heap.append(e)
    i = len(heap)-1
    while i > 0:
        if heap[i] < heap[(i - 1) // 2]:
            heap[(i - 1) // 2], heap[i] = heap[i], heap[(i - 1) // 2]
            i = (i - 1) // 2
        else:
            break
    return heap

def heapify(arr):
    result = []
    for i in range(len(arr)):
        result = addelement(arr[i], result)
    return result

def remove(e, heap):
    for i in range(len(heap)):
        if e == heap[i]:
            heap[-1], heap[i] = heap[i], heap[-1]
            heap.pop()
            if (i*2)+1 > len(heap)-1:
                return heap
            if (i*2)+2 > len(heap)-1:
                if heap[i] > heap[(i*2)+1]:
                    heap[i], heap[(i*2)+1] = heap[(i*2)+1], heap[i]
                    return heap
                else:
                    return heap
            while i <= len(heap):
                children = [heap[(i*2)+1], heap[(i*2)+2]]
                if heap[i] < children[0] and heap[i] < children[1]:
                    break
                low = min(children)
                if low == children[0]:
                    heap[i], heap[(i*2)+1] = heap[(i*2)+1], heap[i]
                    i = (i*2)+1
                elif low == children[1]:
                    heap[i], heap[(i*2)+2] = heap[(i*2)+2], heap[i]
                    i = (i*2)+2
            return heap
    print("404")
    return heap


heap1 = heapify(testarray)
print(heap1)
# heap1 = addelement(6, heap1)
# print(heap1)
# heap1 = remove(7, heap1)
print(heap1)