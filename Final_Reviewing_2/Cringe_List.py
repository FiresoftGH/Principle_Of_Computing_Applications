import random

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def getData(self):
        return self.data

    def setData(self, new_data):
        self.data = new_data

    def getNext(self):
        return self.next

    def setNext(self, new_next):
        self.next = new_next

class UnorderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def append(self, item):
        new_node = Node(item)
        new_node.setNext(self.head)
        self.head = new_node

    def search(self, item):
        current = self.head
        while current is not None:
            if current.getData() == item:
                return True

            else:
                current = current.getNext()

        return False

    def squish(self):
        current = self.head
        while current is not None:
            if current.getData() == current.next.getData():
                print("hello")
                break

            else:
                current = current.getNext()

    def remove(self, item):
        current = self.head
        previous = None

        while current is not None:
            if current.getData() == item:
                break

            else:
                previous = current
                current = current.getNext()

        if previous is None:
            self.head = current.next

        else:
            previous.setNext(current.next)

    def size(self): return print(len(self.printlist()))

    def printlist(self):
        current = self.head
        temp_array = []
        while current is not None:
            temp_array.append(current.getData())
            current = current.next

        print(temp_array)
        return temp_array

single = UnorderedList()
single.printlist()
single.append(1)
single.append(2)
single.printlist()

print(single.search(0))
for x in range(2):

    single.append(2)

single.printlist()

single.remove(1)
single.squish()
single.printlist()





