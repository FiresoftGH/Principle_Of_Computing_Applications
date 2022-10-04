# Ref: https://runestone.academy/ns/books/published/pythonds/BasicDS/ImplementinganUnorderedListLinkedLists.html
# Node Class

class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext

# Test the node class
# temp = Node(93)
# print(temp.getData())

class UnorderedList:
    def __init__(self):
        self.head = None
    
    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
    
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
        
        return found

    def remove(self, item):
        current = self.head
        previous = None
        while not found:
            if current.getData() == item:
                found = True

            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()

        else:
            previous.setNext(current.getNext())

    def squish(self):
        current = self.head
        if current is None:
            return None
        while current.next is not None:
            if current.getData() == current.next.getData():
                operation = current.next.next
                current.next = None
                current.next = operation
            else:
                current = current.next

        return self.head
        
    def printList(self):
        operation = self.head
        while (operation):
            print(operation.data)
            operation = operation.next

    def dble(self):
        current = self.head
        while current != None:
            operation = current.getData()
            new_node = Node(operation)
            new_node.setNext(current.getNext())
            current.setNext(new_node)
            current = current.getNext().getNext()
myList = UnorderedList()
myList.add(1)
myList.add(2)
myList.add(1)
myList.add(1)
myList.dble()
# print(myList.size())
myList.printList()